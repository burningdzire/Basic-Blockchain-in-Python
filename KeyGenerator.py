from Crypto.PublicKey import RSA

key = RSA.generate(2048)
privateKey = key.exportKey()
privateKeyFileObject = open("private.pem", "w")
privateKeyFileObject.write(privateKey)

publicKey = key.publickey().exportKey()
publicKeyFileObject = open("public.pem", "w")
publicKeyFileObject.write(publicKey)
