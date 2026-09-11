#!/usr/bin/env python3
from pathlib import Path
import io
import re
import math
import base64
import zipfile
import struct
import itertools
import string

PNG_PATH = Path("2025-ICO-Q16-ico_img.png")

def rot47(s: str) -> str:
    out = []
    for ch in s:
        o = ord(ch)
        if 33 <= o <= 126:
            out.append(chr(33 + ((o - 33 + 47) % 94)))
        else:
            out.append(ch)
    return "".join(out)

def atbash(s: str) -> str:
    out = []
    for ch in s:
        if "a" <= ch <= "z":
            out.append(chr(ord("z") - (ord(ch) - ord("a"))))
        elif "A" <= ch <= "Z":
            out.append(chr(ord("Z") - (ord(ch) - ord("A"))))
        else:
            out.append(ch)
    return "".join(out)

def caesar(s: str, shift: int) -> str:
    out = []
    for ch in s:
        if "a" <= ch <= "z":
            out.append(chr((ord(ch) - 97 + shift) % 26 + 97))
        elif "A" <= ch <= "Z":
            out.append(chr((ord(ch) - 65 + shift) % 26 + 65))
        else:
            out.append(ch)
    return "".join(out)

def xor_repeat(data: bytes, key: bytes) -> bytes:
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

def vig95_dec(text: str, key: str) -> str:
    alpha = "".join(chr(i) for i in range(32, 127))
    idx = {c: i for i, c in enumerate(alpha)}
    out = []
    ki = 0
    for ch in text:
        if ch in idx:
            k = key[ki % len(key)]
            if k in idx:
                out.append(alpha[(idx[ch] - idx[k]) % 95])
                ki += 1
            else:
                out.append(ch)
        else:
            out.append(ch)
    return "".join(out)

def affine95_dec(text: str, a: int, b: int) -> str:
    alpha = "".join(chr(i) for i in range(32, 127))
    idx = {c: i for i, c in enumerate(alpha)}
    out = []
    for ch in text:
        if ch in idx:
            x = idx[ch]
            out.append(alpha[(a * (x - b)) % 95])
        else:
            out.append(ch)
    return "".join(out)

def b64_clean_decode(s: str) -> list[str]:
    cleaned = "".join(ch for ch in s if ch in string.ascii_letters + string.digits + "+/=")
    outs = []
    for pad in ("", "=", "==", "==="):
        try:
            outs.append(base64.b64decode(cleaned + pad, validate=False).decode("latin1", errors="ignore"))
        except Exception:
            pass
    return outs

def extract_zip_embedded(png_bytes: bytes):
    sig = b"PK\x03\x04"
    pos = png_bytes.find(sig)
    if pos == -1:
        return None
    zip_bytes = png_bytes[pos:]
    zf = zipfile.ZipFile(io.BytesIO(zip_bytes))
    return zf

def printable_runs(bs: bytes, minlen: int = 4):
    return re.findall(rbf"[\x20-\x7e]{{{minlen},}}", bs)

def main():
    data = PNG_PATH.read_bytes()

    # 1) ZIP appended after PNG IEND
    zf = extract_zip_embedded(data)
    if zf:
        print("[+] Embedded ZIP members:")
        for name in zf.namelist():
            raw = zf.read(name)
            print(f"    - {name} ({len(raw)} bytes)")
            print(raw.decode("latin1", errors="replace"))

    # 2) Parse PLTE chunk and gather printable substrings
    off = 8
    plte = None
    while off + 8 <= len(data):
        length = struct.unpack(">I", data[off:off+4])[0]
        ctype = data[off+4:off+8]
        if ctype == b"PLTE":
            plte = data[off+8:off+8+length]
            break
        off += 12 + length

    if plte is None:
        print("[-] No PLTE chunk found")
        return

    # Candidate keys from printable runs in PLTE
    runs = [m.group() for m in re.finditer(rb"[\x20-\x7e]{4,}", plte)]
    keys = set()
    for r in runs:
        for sublen in range(4, min(17, len(r) + 1)):
            for i in range(len(r) - sublen + 1):
                keys.add(r[i:i+sublen])
        keys.add(r[::-1])
        rr = bytearray()
        for c in r:
            rr.append(33 + ((c - 33 + 47) % 94) if 33 <= c <= 126 else c)
        keys.add(bytes(rr))

    cipher = zf.read("flag.txt") if zf and "flag.txt" in zf.namelist() else None
    if cipher is None:
        print("[-] flag.txt missing")
        return

    text = cipher.decode("latin1", errors="ignore")

    seen = set()
    candidates = []

    # 3) Try XOR-repeat with PLTE-derived keys
    for key in keys:
        try:
            x = xor_repeat(cipher, key)
            s = x.decode("latin1", errors="ignore")
            for t in [s, s[::-1], rot47(s), atbash(s)] + [caesar(s, sh) for sh in range(26)]:
                candidates.append(t)
                candidates.extend(b64_clean_decode(t))
        except Exception:
            pass

    # 4) Try printable Vigenère with PLTE-derived keys
    for key in keys:
        k = key.decode("latin1", errors="ignore")
        try:
            s = vig95_dec(text, k)
            for t in [s, s[::-1], rot47(s), atbash(s)] + [caesar(s, sh) for sh in range(26)]:
                candidates.append(t)
                candidates.extend(b64_clean_decode(t))
        except Exception:
            pass

    # 5) Try affine over printable ASCII
    valid_as = [a for a in range(1, 95) if math.gcd(a, 95) == 1]
    for a in valid_as:
        for b in range(95):
            try:
                s = affine95_dec(text, a, b)
                for t in [s, s[::-1], rot47(s), atbash(s)] + [caesar(s, sh) for sh in range(26)]:
                    candidates.append(t)
                    candidates.extend(b64_clean_decode(t))
            except Exception:
                pass

    # 6) Print unique brace-enclosed candidates
    out = []
    for s in candidates:
        if not isinstance(s, str):
            continue
        if s in seen:
            continue
        seen.add(s)
        if re.search(r"[A-Za-z0-9_]{2,12}\{[^}]{3,120}\}", s):
            out.append(s)

    print("\n[+] Brace-enclosed candidates:")
    for s in sorted(out, key=len):
        print(s)

if __name__ == "__main__":
    main()
