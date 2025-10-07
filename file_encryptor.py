import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import getpass
def generar_clave(password, sal):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=sal,
        iterations=480000
    )
    return kdf.derive(password.encode())
def cifrar_archivo(ruta, password):
    try:
        with open(ruta, 'rb') as f:
            datos = f.read()
        sal = os.urandom(16)
        clave = generar_clave(password, sal)
        aes = AESGCM(clave)
        nonce = os.urandom(12)
        datos_cifrados = aes.encrypt(nonce, datos, None)
        nueva_ruta = ruta + ".enc"
        with open(nueva_ruta, 'wb') as f:
            f.write(sal)
            f.write(nonce)
            f.write(datos_cifrados)
        print("Archivo cifrado como:", nueva_ruta)
    except FileNotFoundError:
        print("No se encontró el archivo:", ruta)
    except Exception as e:
        print("Error al cifrar:", e)
def descifrar_archivo(ruta, password):
    try:
        with open(ruta, 'rb') as f:
            sal = f.read(16)
            nonce = f.read(12)
            datos_cifrados = f.read()
        clave = generar_clave(password, sal)
        aes = AESGCM(clave)
        datos_descifrados = aes.decrypt(nonce, datos_cifrados, None)

        nueva_ruta = ruta[:-4] + ".dec"
        with open(nueva_ruta, 'wb') as f:
            f.write(datos_descifrados)
        print("Archivo descifrado como:", nueva_ruta)
    except FileNotFoundError:
        print("No se encontró el archivo cifrado:", ruta)
    except Exception as e:
        print("Error al descifrar:", e)
def main():
    print("=== Programa para Cifrar o Descifrar Archivos ===")
    opcion = input("¿Deseas cifrar (c) o descifrar (d)? ").lower()
    if opcion not in ['c', 'd']:
        print("Opción no válida.")
        return
    ruta = input("Ingresa la ruta completa del archivo (nombre completo):")
    password = getpass.getpass("Contraseña: ")
    if opcion == 'c':
        cifrar_archivo(ruta, password)
    else:
        descifrar_archivo(ruta, password)
if __name__ == "__main__":
    main()
