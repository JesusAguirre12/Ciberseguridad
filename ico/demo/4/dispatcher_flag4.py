from client import *
import sys
import os

FLAG4 = os.getenv('FLAG4', 'ICO{example_flag_4}')

baseurl = f"http://{sys.argv[2]}"
flag4_username, flag4_password = create_random_credentials()

user = User(baseurl)
user.register(flag4_username, flag4_password)
resp = user.add_note('Note for flag 4', 'This is a note for flag 4')
note_id = resp.text.split('Note ')[1].split(' added')[0]
user.add_comment(note_id, FLAG4)