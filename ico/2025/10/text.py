#!/usr/bin/env python3
from pathlib import Path
import io
import zipfile

PNG = Path("2025-ICO-Q16-ico_img.png")

data = PNG.read_bytes()

# PNG ends with IEND, but this file has extra ZIP data appended after it.
zip_sig = b"PK\x03\x04"
pos = data.find(zip_sig)
if pos == -1:
    raise SystemExit("No ZIP signature found after the PNG data")

zip_data = data[pos:]
zf = zipfile.ZipFile(io.BytesIO(zip_data))

for name in zf.namelist():
    print(f"[+] Found: {name}")
    content = zf.read(name)
    print(content.decode("utf-8", errors="replace"))
