import hashlib
from cryptography.fernet import Fernet
import base64

username_trial=b"BENNETT"

c=hashlib.sha256(username_trial).hexdigest()

print(c)
