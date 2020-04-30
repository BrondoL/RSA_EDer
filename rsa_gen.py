from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random

random_generator = Random.new().read
key = RSA.generate(1024, random_generator)

f = open('public.pem', 'wb')
f.write(key.publickey().exportKey('PEM'))
f.close()

f = open('private.pem', 'wb')
f.write(key.exportKey('PEM'))
f.close()

print("Public key dan Private key Berhasil dibuat")