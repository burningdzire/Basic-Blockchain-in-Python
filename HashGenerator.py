import hashlib

def HashGenerator(input):
    result = hashlib.sha256(input.encode())
    return result.hexdigest()
