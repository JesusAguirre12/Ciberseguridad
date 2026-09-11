import base64, zlib
data = "eJwty0sKgCAQANC7zFrCGGPMy4TkJII_1FbR3XPR9sF7IBbv2YGBy8bOIKCMenQ-G4-JO0n92wiJ-7CpgllJEyqpFC4KCVFuAu7OLdvEM1mXQob3A0aRHF0.aoimmw.CGyzTkflZyZVmT06vd9zvXGJEgQ"
decoded = zlib.decompress(base64.urlsafe_b64decode(data + '=='))
print(decoded)
