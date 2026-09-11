import csv
import subprocess
import sys
import hashlib   
# Define the expected number of fields based on your header
EXPECTED_FIELD_COUNT = 11
LOG_FILE_PATH = 'audit_log.csv' # The file containing the log data
   
SESSION_DIGEST = "8e93f409a586a75fe398afaabd2eedccc82e18d7841acf7521ba3f1635c8dbc1"
LOG_ID_DIGEST = "04b8231d91b5add153aed8c7a7dddb60feb663208dd181d8f3dde64a1b33c569"
HASH_DIGEST = "51c5a864240c9a2301b5f4882da6fd06c763523a351b979c2661d6da91302b4b"
FLAG_CIPHERTEXT = bytes.fromhex(
    "7ff70670bb487291c7324ee19f06bde245bc2b145be07c54ce2adba32361cb994d26d791f1e232d1"
)


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()


def keystream(key, size):
    out = b""
    counter = 0
    while len(out) < size:
        out += hashlib.sha256(key + counter.to_bytes(4, "big")).digest()
        counter += 1
    return out[:size]


def call_checker_script(log_id,session,has):
    key = hashlib.sha256(
        ("audit-log:v1:" + session + "\0" + log_id + "\0" + has).encode()
    ).digest()
    flag = bytes(a ^ b for a, b in zip(FLAG_CIPHERTEXT, keystream(key, len(FLAG_CIPHERTEXT))))
    print(flag)


 
   
def process_log_data(file_path):
    valid_entries = []
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            # Using csv.reader to handle potential quoting within fields
            # We are not using csv.DictReader because the header format is inconsistent
            reader = csv.reader(csvfile)

            # Skip the header line if it's always present and inconsistent
            # A more robust way might be to check if the first line has the expected field count
            try:
                first_line = next(reader)
                if len(first_line) != EXPECTED_FIELD_COUNT:
                     # If the first line itself doesn't match, it might be actual data
                     # Or the header is missing/malformed.
                     # For now, let's re-process it as if it were data if it's not the header
                     # A safer bet is to assume the first line *is* the header to skip if its length is off.
                     # If your actual logs *start* with data lines that have EXACTLY 11 fields,
                     # you might need to adjust this logic.
                     # For this example, let's assume the first line IS the header we need to skip
                     # *if* it doesn't match the expected count, or if it's just header text.
                     # If the first line IS data and has 11 fields, it will be processed below.
                     # Let's refine: process *all* lines that have the correct field count.
                     pass # Will re-process this line below if it's valid data.
   
            except StopIteration:
                print("File is empty.")
                return
   
            # Re-open or reset reader to process all lines, including the first if it's valid data
            csvfile.seek(0) # Go back to the start of the file
            reader = csv.reader(csvfile) # Re-create reader

            # Now process every line
            for line_num, row in enumerate(reader):
            
                if len(row) == EXPECTED_FIELD_COUNT:
                    try:
                        log_id = row[0]
                        # timestamp = row[1] # Not needed for checker.py
                        # user_id = row[2] # Not needed
                        # user_role = row[3] # Not needed
                        session_id = row[4]
                        # turn = row[5] # Not needed
                        # guard_score = row[6] # Not needed
                        # tool_called = row[7] # Not needed
                        # tool_args = row[8] # Not needed
                        # decision = row[9] # Not needed
                        output_hash = row[10]
                            # Basic validation: Ensure extracted fields are not empty strings
                        if log_id and session_id and output_hash:
                            entry_data = {
                                "log_id": log_id,
                                "session_id": session_id,
                                "output_hash": output_hash
                            }
                            valid_entries.append(entry_data)
                            print(f"Valid entry found: Log ID={log_id}, Session={session_id}, Hash={output_hash}")
                            call_checker_script(log_id,session_id,output_hash)
                        else:
                            print(f"Line {line_num + 1}: Skipped (contains empty required fields).")
                    except IndexError:
                        # This should ideally not happen if len(row) == EXPECTED_FIELD_COUNT
                        print(f"Line {line_num + 1}: Skipped (unexpected IndexError during field access).")
                else:
                    # This line does not have the expected number of fields
                    print(f"Line {line_num + 1}: Skipped")
   
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1) # Exit the script if the file is not found
    except Exception as e:
        print(f"An unexpected error occurred while reading '{file_path}': {e}")
        sys.exit(1)
        return valid_entries
  


def checker_script(log_id, session_id, output_hash):
    """Calls checker.py using subprocess.run"""
    print(f"\n--- Calling checker.py ---")
    print(f"  Arguments: --log-id={log_id}, --session={session_id}, --hash={output_hash}")

    # Construct the command as a list
    command = [
        sys.executable, # Use the same Python interpreter that's running this script
        'checker.py',   # The script to run
        '--log-id', log_id,
        '--session', session_id,
        '--hash', output_hash
    ]

    try:
        print("-----------VALID-----------")
        # Execute the command
        # capture_output=True captures stdout and stderr
        # text=True decodes stdout/stderr as text
        result = subprocess.run(command, capture_output=True, text=True, check=True)

        print(-------------------"checker.py stdout:-------------------")
        print(result.stdout)
        if result.stderr:
            print("checker.py stderr:")
            print(result.stderr)
        print("--- checker.py finished ---")

    except FileNotFoundError:
        print(f"Error: 'checker.py' not found. Make sure it's in the same directory or in your PATH.")
    except subprocess.CalledProcessError as e:
        # This catches errors if checker.py exits with a non-zero status code
        print(f"Error calling checker.py:")
        print(f"  Command: {' '.join(e.cmd)}")
        print(f"  Return code: {e.returncode}")
        print(f"  stdout:\n{e.stdout}")
        print(f"  stderr:\n{e.stderr}")
    except Exception as e:
        print(f"An unexpected error occurred during subprocess execution: {e}")

  
if __name__ == "__main__":
    print(f"Processing log data from '{LOG_FILE_PATH}'...")
    valid_log_entries = process_log_data(LOG_FILE_PATH)

    if not valid_log_entries:
        print("\nNo valid log entries found to process.")
    else:
        print(f"\nFound {len(valid_log_entries)} valid entries. Attempting to call checker.py for each.")
        for entry in valid_log_entries:
            # Call the checker script for each valid entry
            call_checker_script(entry['log_id'], entry['session_id'], entry['output_hash'])
        print("\nProcessing complete.")
