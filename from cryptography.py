pip install cryptography
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_message(key, message):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt_message(key, encrypted_message):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message

# Contoh penggunaan
if __name__ == "__main__":
    # Generate Key
    key = generate_key()
    print("Generated Key:", key)

    # Pesan yang akan dienkripsi
    message = input ("masukkan pesan yang akan dienkripsi :")

    # Enkripsi pesan
    encrypted_message = encrypt_message(key, message)
    print("Encrypted Message:", encrypted_message)

    # Dekripsi pesan
    decrypted_message = decrypt_message(key, encrypted_message)
    print("Decrypted Message:", decrypted_message)
