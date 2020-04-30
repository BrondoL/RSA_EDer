from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

public = input("Masukan file public key: ")
f = open(public, "rb")
key = RSA.importKey(f.read())

msg = input("Masukkan pesan yang ingin diencrypt: ")
f = open(msg, "r")
plaintext = f.read()

encryptor = PKCS1_OAEP.new(key)
x = encryptor.encrypt(plaintext.encode())

f = open('chipertext.txt', 'wb')
f.write(x)
f.close()

print("Pesan berhasil diencrypt")