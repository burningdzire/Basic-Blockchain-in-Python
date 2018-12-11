import hashlib
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from base64 import b64encode, b64decode


def HashGenerator(input):
    result = hashlib.sha256(input.encode())
    return result.hexdigest()


