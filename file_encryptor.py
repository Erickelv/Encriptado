import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import getpass 
def generate_key_from_password(password: str, salt: bytes) -> bytes:
    """
    Genera una clave criptográfica segura a partir de una contraseña y una sal.
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  
        salt=salt,
        iterations=480000, 
    )
    return kdf.derive(password.encode())

def encrypt_file(file_path: str, password: str):
    """
    Cifra un archivo usando la contraseña proporcionada.
    """
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        salt = os.urandom(16)
        key = generate_key_from_password(password, salt)
        aesgcm = AESGCM(key)
        nonce = os.urandom(12) 
        encrypted_data = aesgcm.encrypt(nonce, data, None)
        encrypted_file_path = file_path + ".enc"
        with open(encrypted_file_path, 'wb') as f:
            f.write(salt)
            f.write(nonce)
            f.write(encrypted_data)
        
        print(f" ¡Éxito! Archivo cifrado guardado como: {encrypted_file_path}")

    except FileNotFoundError:
        print(f" Error: El archivo '{file_path}' no fue encontrado.")
    except Exception as e:
        print(f" Ocurrió un error inesperado durante el cifrado: {e}")

def decrypt_file(encrypted_file_path: str, password: str):
    """
    Descifra un archivo .enc usando la contraseña correcta.
    """
    try:
        with open(encrypted_file_path, 'rb') as f:
            salt = f.read(16)
            nonce = f.read(12)
            encrypted_data = f.read()
        key = generate_key_from_password(password, salt)
        aesgcm = AESGCM(key)
        decrypted_data = aesgcm.decrypt(nonce, encrypted_data, None)
        decrypted_file_path = encrypted_file_path.replace('.enc', '.decrypted')
        with open(decrypted_file_path, 'wb') as f:
            f.write(decrypted_data)
            
        print(f" ¡Éxito! Archivo descifrado guardado como: {decrypted_file_path}")

    except FileNotFoundError:
        print(f" Error: El archivo cifrado '{encrypted_file_path}' no fue encontrado.")
    except Exception as e:
        print(f" Error al descifrar. ¿Es la contraseña correcta? Detalles: {e}")
def main():
    print("--- Herramienta de Cifrado y Descifrado de Archivos ---")
    
    choice = input("¿Deseas (c)ifrar o (d)escifrar un archivo? ").lower()

    if choice not in ['c', 'd']:
        print("Opción no válida. Saliendo del programa.")
        return

    file_path = input("Introduce la ruta completa del archivo: ")
    password = getpass.getpass("Introduce tu contraseña segura: ")

    if choice == 'c':
        encrypt_file(file_path, password)
    elif choice == 'd':
        decrypt_file(file_path, password)
if __name__ == "__main__":
    main()
