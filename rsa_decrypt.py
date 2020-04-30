from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

private = input("Masukan file private key: ")
f = open(private, "rb")
key = RSA.importKey(f.read())

msg = input("Masukkan pesan yang ingin didecrypt: ")
f = open(msg, "rb")
chipertext = f.read()

decryptor = PKCS1_OAEP.new(key)
plaintext = decryptor.decrypt(chipertext)

f = open('plaintext.txt', 'w')
f.write(plaintext.decode("utf-8"))
f.close()

print("Pesan berhasil didecrypt")