from cryptography.fernet import Fernet
import os

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename="secret.key"):
    with open(filename, "wb") as key_file:
        key_file.write(key)

def load_key(filename="secret.key"):
    return open(filename, "rb").read()

def encrypt_script(script, key):
    f = Fernet(key)
    encrypted_script = f.encrypt(script.encode())
    return encrypted_script

def decrypt_script(encrypted_script, key):
    f = Fernet(key)
    decrypted_script = f.decrypt(encrypted_script).decode()
    return decrypted_script

# Generate and save a key
key = generate_key()
save_key(key)
input_file = input("Masukkan nama file .py yang ingin di encrypt: ")

# Read the script from a file or provide it as a string
with open(input_file, "r") as script_file:
    original_script = script_file.read()

# Encrypt the script
encrypted_script = encrypt_script(original_script, key)

# Save the encrypted script to a new file
with open("output.py", "wb") as encrypted_file:
    encrypted_file.write(encrypted_script)

# Example of decrypting the script
loaded_key = load_key()
decrypted_script = decrypt_script(encrypted_script, loaded_key)

# Print the decrypted script
print(decrypted_script)
