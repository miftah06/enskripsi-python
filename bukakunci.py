from cryptography.fernet import Fernet

def load_key(filename="secret.key"):
    return open(filename, "rb").read()

def decrypt_script(encrypted_script, key):
    f = Fernet(key)
    decrypted_script = f.decrypt(encrypted_script).decode()
    return decrypted_script

# Load kunci enkripsi
loaded_key = load_key()

# Baca skrip yang dienkripsi dari file
with open("output.py", "rb") as encrypted_file:
    encrypted_script = encrypted_file.read()

# Dekripsi skrip
decrypted_script = decrypt_script(encrypted_script, loaded_key)

# Print skrip yang sudah didekripsi
print(decrypted_script)
