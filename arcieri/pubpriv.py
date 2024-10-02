from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

"""
# Generating RSA Key Pair
key_pair = RSA.generate(2048)
public_key = key_pair.publickey()
print(public_key.export_key())
print(key_pair.export_key)
"""

sPub="-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvxetWRL2xqjcLSSBoV0R\ng0U3msq6OAohA/bzHGLU/YxtC1cq2AAhq9JS6IR6qnQyfWMR4FyLotyvqAVxENRU\nil9rzYVdIkg4pJKDtIx/ws3+xC5MbOoux+HHl0S0cGLp+J3XgtqhmHxKStNOWbe4\nA985HOvJpOoPRiABmjgtn+xTGaXYFv/EMlTQlqanD9WMCVRrHpxU4oUpJR/Zx1KH\nqslniA4DpUpjzkheSeRGsww4Brz6l5HP9GWiCOZ/o2mUjtOcvPFK+Y4eaDjWbXaU\nV46RcjJgSAEV1LruMRqpmeX7fRCaHMelHWWknyzYPvNj+q6lGi96hOkJadr+ei6x\n8wIDAQAB\n-----END PUBLIC KEY-----"
sPriv="-----BEGIN RSA PRIVATE KEY-----\nMIIEogIBAAKCAQEAvxetWRL2xqjcLSSBoV0Rg0U3msq6OAohA/bzHGLU/YxtC1cq\n2AAhq9JS6IR6qnQyfWMR4FyLotyvqAVxENRUil9rzYVdIkg4pJKDtIx/ws3+xC5M\nbOoux+HHl0S0cGLp+J3XgtqhmHxKStNOWbe4A985HOvJpOoPRiABmjgtn+xTGaXY\nFv/EMlTQlqanD9WMCVRrHpxU4oUpJR/Zx1KHqslniA4DpUpjzkheSeRGsww4Brz6\nl5HP9GWiCOZ/o2mUjtOcvPFK+Y4eaDjWbXaUV46RcjJgSAEV1LruMRqpmeX7fRCa\nHMelHWWknyzYPvNj+q6lGi96hOkJadr+ei6x8wIDAQABAoIBAF46EqRlkYIMKeWo\nprMm7UfJjc2qQYD4nacS0nYg1d3grLR22w1/oxrSr0cwbDw459ykSWBUwhYgtA0q\nAcLGsJk6zDGfnXkWG7gq9v7EeQtaAFJEcjMSltbBImYY3tC8NZr+WhKQNDa4svmK\nkIv056whGkyEh/3l3Ho7tg6RvQ2p41sB0f2WPmNg8QwuiqlNLYdzRsTZlXzYAmem\no3mpUq9J0T5Ca3mY1D5NJ2Uub6JBlVAtWl1LUBtFG5vXcWfOwy5iAfxmzGPwDlK4\n5uV/kUY0u2Dek2b8/QC/bLj3tgfR2FnQCcpDnfiVkbkUKLSQDFKFSs+75sXIdiKh\n9162m4ECgYEAx6lybVEc4iJS/WMiPp7GU8LwcR/1bbFZ4AybfKfF99jlBoA2vGvV\nwRnSxp9TzJtcJcpCbpJMterz5NUau9kzR0PKo6a+N765tB3RT+5PxuHQdSETnRGf\nWSqCsuSw2q7qf+pMoNvu4fyBuiKuRaTpX7DQeCfcfawPrPk/I7T9I0MCgYEA9QM4\nOcH8pRVuUXckBmcsonwwVzeXQ0mGS/tjaoZFtOuucYHe3o/VC3gl0pX0CAN2NsoJ\nFkg2ImG/ILlVNqlZ7R0cbQrZbRKdg+dLFtgT5SXX9Gj/KxodIm4bGXw5x1EUQrq4\nSMUIvA+Hh6Ifr/hNYGHv8QSmRe+TJKVmENK1U5ECgYAdzrY+i7V8LROmsH4USy/g\noWG0AclqLuf0Au3Tllh/v+mxJsMFLjQjN++3p2GjUi5XlfKE/2JkZkczCn2LPcni\nAcTm2aXcPKUMtsbg3/sY/e1ZDy8Wa+MWNLp+apXcj/CCWEBIY40uP7w+RZ8u1ofg\nuUzmI01PlbhhYnSCqCqCcQKBgFU7L334G3kaAWxZc7C+h2pmpTJR5k7D7vHTm3vd\nBbawHdjigrMNeeEphI7DF0cKXT8l/Q9BQ4OmWSR7FEeVlfDEJbVRBt3Ikf7moNpr\nhFA8X+ln9Qv7Y5MslkTBUCAj9lZYOe8mi6lQBaeLIFbIm7Ihn6RKJ8VAWAFxgBXu\nFqHhAoGAU0WoxunbZmrKHdXWksYpl3Y7kQ67t0zxz1anTr3s07HapJL7BDaO1DnI\n+0dOpgLGmn3F3pOnftpW1o708P2hf2edrAQG8k997Nuo2zS6W2sO3VaSYfW8Gkpo\n5fZRyY+mVtybXZw5nW6+gm48nYHSxR8Qy2ulHcmMKQywRqPzOTY=\n-----END RSA PRIVATE KEY-----"
key_pair=RSA.import_key(sPriv)

public_key=RSA.import_key(sPub)
# Function to encrypt message
def encrypt_message(message, pub_key):
    cipher = PKCS1_OAEP.new(pub_key)
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    return base64.b64encode(encrypted_message).decode("utf-8")


# Function to decrypt message
def decrypt_message(encrypted_message, priv_key):
    cipher = PKCS1_OAEP.new(priv_key)
    decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_message.decode("utf-8")

"""
# Example usage
message = "This is a secret message"
encrypted_message = encrypt_message(message, public_key)
decrypted_message = decrypt_message(encrypted_message, key_pair)


print("Original Message:", message)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
"""

#LO FATE VOI
# Ora, utilizzando la chiave pubblica di un vostro collega,
# dovete inviargli un messaggio cifrato
# il vostro collega lo potrà decifrare con la propria chiave privata
public_key_collega = RSA.import_key("-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAm00GoIe5Sdwo0S/CI4vB\n0taa9B6Y07J704scX3r4pEEpWMd2F6sCv+V8KZ4ws7UokNUcKArRC6MLrT+RlUN3\njFM5CdfY1PgpHXP6M1qylmhX3j9Gsp7UkFotJ1svCddfNw07zKr4eMwyo6VdycAr\nBmWDaCnS1GR8+0bIbUYN/qZQkJrncmom6Qxs+ok1mkEyMUlw8D55rKQoSN+DgLoI\nktt879QJZTQVdu9bMUWmLY/+tLd8vIEypXtB7r0w90PFk0AoFs+yYO8WTmsbrhSb\niMae+s+9OshnPiJDyrgObqJBFR3V5XRPBkeUXEngFDMtnoJHVuBujKlIKaq5a2hD\noQIDAQAB\n-----END PUBLIC KEY-----")
message = "COCOOOOOOO"
encrypted_message = encrypt_message(message, public_key_collega)
print("Encrypted Message:", encrypted_message)

#LO FA IL VOSTRO COLLEGA
# e lo inviate come stringa al vostro collega
# Il vostro collega riceve il messaggio cifrato
cifrato = "uffdYupKJVAJfVHqX8RrrFOMGeCFj2II8vJa3rrwwgAxocUprmJ3dR3AgOlxXSEM6iXvuBClta3+ZeOfPQ+Gq8eOP8ZtbR95b4qeHCmf0mSk3+uvib8l5Cqg1eXskujDCWju4qjVIyXUah3+dDzqzbcbUN+F1evDUU1VeQ7kpPJWnEpsnRW0OisKAiGVYrSANQFa8WuERM/fOaJdiFK/VwmScbnephSueX/sxXEFbonrAimXaOrKdM/PZkiXIS1hd+WPvhtWWTqM6nrFPC56PMgXjzcL41MhapnL1hhyg83Fi9OCldW4R3yXrdid5XpTHl+lvygHWVB/R+hLOLOiFg=="
decifrato = decrypt_message(cifrato, key_pair)
print("Il messaggio decifrato: ", decifrato)