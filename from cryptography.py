from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher = Fernet(key)
def encrypt_message(message):
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message
def decrypt_message(encrypted_message):
    decrypted_message = cipher.decrypt(encrypted_message).decode()
    return decrypted_message
message = "Ini adalah pesan rahasia"
encrypted_message = encrypt_message(message)
print("Pesan terenkripsi:", encrypted_message)

decrypted_message = decrypt_message(encrypted_message)
print("Pesan terdekripsi:", decrypted_message)