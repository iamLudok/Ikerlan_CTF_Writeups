import random

def encrypt(message, key_seed):
    random.seed(key_seed)
    ciphertext = ""
    for byte in message:
        key_byte = random.randint(0, 255)
        encrypted_byte = byte ^ key_byte
        ciphertext += f"{encrypted_byte:02x}"
    return ciphertext

if __name__ == "__main__":
    msg = str(input("Mensaje a encriptar\n")).encode()
    SECRET_KEY_SEED = 1337
    encrypted = encrypt(msg, SECRET_KEY_SEED)
    print(f"Mensaje cifrado: {encrypted}")