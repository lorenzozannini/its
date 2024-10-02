from Crypto.Cipher import AES 
import base64

# Function to pad the message to be multiple of 16 bytes
def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

# Encryption
def encrypt(plain_text, key):
    cipher = AES.new(pad(key).encode('utf-8'), AES.MODE_ECB)
    encrypted_text = cipher.encrypt(pad(plain_text).encode('utf-8'))
    return base64.b64encode(encrypted_text).decode('utf-8')

# Decryption
def decrypt(encrypted_text, key):
    cipher = AES.new(pad(key).encode('utf-8'), AES.MODE_ECB)
    decrypted_text = cipher.decrypt(base64.b64decode(encrypted_text)).decode('utf-8').strip()
    return decrypted_text

"""
# Example usage
key = "ThisIsASecretKey"
plain_text = "0123456780123456"
encrypted_text = encrypt(plain_text, key)
decrypted_text = decrypt(encrypted_text, key)

print("Plain Text:", plain_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
"""

#prova di decifra brute force

key = "XXXXIsASecretKey"
en = "OgJuOYJZT0FDb47DBOkNgA=="
for c1 in "abcdefghilmnopqrstuvzABCDEFGHILMNOPQRSTUVZ":
    for c2 in "abcdefghilmnopqrstuvzABCDEFGHILMNOPQRSTUVZ":
        for c3 in "abcdefghilmnopqrstuvzABCDEFGHILMNOPQRSTUVZ":
            for c4 in "abcdefghilmnopqrstuvzABCDEFGHILMNOPQRSTUVZ":
                key= f"{c1}{c2}{c3}{c4}IsASecretKey"
                try: 
                    decrypt(en, key)
                    print(f"Chiave: {key} parola: {decrypt(en, key)}")
                except:
                    continue
#MiNeIsASecretKey
