# File Encryption Tool / Herramienta de Cifrado de Archivos 

---
<a name="español"></a>

## Este es un script de línea de comandos simple y seguro para cifrar and descifrar archivos utilizando una contraseña. El programa crea una copia cifrada de cualquier archivo, protegiéndolo con un cifrado robusto, y solo puede ser descifrado con la contraseña correcta.

### Características

* **Cifrado Fuerte:** Utiliza **AES-256 en modo GCM**, un estándar de la industria para el cifrado simétrico que garantiza tanto la confidencialidad como la integridad de los datos.
* **Seguridad Basada en Contraseña:** Genera una clave de cifrado robusta a partir de la contraseña del usuario utilizando el algoritmo **PBKDF2 con SHA-256**, lo que mitiga los ataques de fuerza bruta y de diccionario.
* **Fácil de Usar:** Una interfaz interactiva en la consola guía al usuario a través del proceso de cifrado y descifrado.
* **No Destructivo:** El script no modifica ni elimina el archivo original, permitiendo una verificación segura antes de eliminar los datos sensibles.

### Tecnologías Utilizadas 

* **Lenguaje: Python 3**
    * **¿Por qué?** Python es un lenguaje versátil, fácil de leer y cuenta con un ecosistema de librerías de primer nivel para casi cualquier propósito, incluida la ciberseguridad.
* **Librería: `cryptography`**
    * **¿Por qué?** Es la biblioteca de criptografía estándar y más recomendada en Python, mantenida por la *Python Cryptographic Authority* (PyCA). Utilizar esta librería garantiza que se están implementando algoritmos criptográficos de forma correcta y segura, evitando errores comunes que podrían comprometer la seguridad. Proporciona abstracciones de alto nivel que son seguras por defecto.

### Instalación y Uso 

Sigue estos pasos para poner en marcha el programa en tu máquina local.

#### Prerrequisitos

* Tener **Python 3** instalado en tu sistema. 

#### Pasos

1.  **Clona o descarga este repositorio** en tu máquina.
2.  **Abre una terminal** en la carpeta del proyecto.
3.  **Crea y activa un entorno virtual.** Esto es una buena práctica para aislar las dependencias del proyecto.
    ```bash
    # Crear el entorno virtual
    python -m venv venv
    ```
    ```bash
    # Activar en Windows (PowerShell)
    .\venv\Scripts\activate
    ```
    ```bash
    # Activar en macOS/Linux
    source venv/bin/activate
    ```
    *Nota: Si estás en PowerShell y recibes un error de ejecución de scripts, ejecuta primero `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`.*
4.  **Instala las dependencias necesarias.**
    ```bash
    pip install cryptography
    ```
5.  **Ejecuta el script.**
    ```bash
    python file_encryptor.py
    ```
    El programa te pedirá que elijas una opción (cifrar o descifrar), que proporciones la ruta del archivo y que introduzcas una contraseña segura.

### Flujo de Trabajo de Seguridad Recomendado 

Para garantizar la seguridad de tus datos, sigue este proceso:

1.  **Cifra** tu archivo original (ej. `datos_secretos.txt`) para crear la versión cifrada (`datos_secretos.txt.enc`).
2.  **Verifica** que el proceso fue exitoso descifrando el archivo `datos_secretos.txt.enc` para asegurarte de que puedes recuperar la información con tu contraseña.
3.  **Elimina** el archivo original (`datos_secretos.txt`) solo después de haber verificado que el archivo cifrado es correcto y accesible.

-------------

## This is a simple and secure command-line script to encrypt and decrypt files using a password. The program creates an encrypted copy of any file, protecting it with robust encryption, and can only be decrypted with the correct password.

### Features

* **Strong Encryption:** Uses **AES-256 in GCM mode**, an industry standard for symmetric encryption that ensures both confidentiality and data integrity.
* **Password-Based Security:** Generates a robust encryption key from the user's password using the **PBKDF2 with SHA-256** algorithm, which mitigates brute-force and dictionary attacks.
* **Easy to Use:** An interactive console interface guides the user through the encryption and decryption process.
* **Non-Destructive:** The script does not modify or delete the original file, allowing for a safe verification before removing sensitive data.

### Technologies Used 

* **Language: Python 3**
    * **Why?** Python is a versatile, easy-to-read language with a first-class library ecosystem for almost any purpose, including cybersecurity.
* **Library: `cryptography`**
    * **Why?** It is the standard and most recommended cryptography library in Python, maintained by the *Python Cryptographic Authority* (PyCA). Using this library ensures that cryptographic algorithms are implemented correctly and securely, avoiding common mistakes that could compromise security. It provides high-level abstractions that are secure by default.

### Installation and Usage 

Follow these steps to get the program running on your local machine.

#### Prerequisites

* You must have **Python 3** installed on your system. 

#### Steps

1.  **Clone or download this repository** to your machine.
2.  **Open a terminal** in the project folder.
3.  **Create and activate a virtual environment.** This is a best practice to isolate project dependencies.
    ```bash
    # Create the virtual environment
    python -m venv venv
    ```
    ```bash
    # Activate on Windows (PowerShell)
    .\venv\Scripts\activate
    ```
    ```bash
    # Activate on macOS/Linux
    source venv/bin/activate
    ```
    *Note: If you are on PowerShell and get a script execution error, first run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`.*
4.  **Install the necessary dependencies.**
    ```bash
    pip install cryptography
    ```
5.  **Run the script.**
    ```bash
    python file_encryptor.py
    ```
    The program will prompt you to choose an option (encrypt or decrypt), provide the file path, and enter a secure password.

### Recommended Security Workflow 

To ensure the security of your data, follow this process:

1.  **Encrypt** your original file (e.g., `secret_data.txt`) to create the encrypted version (`secret_data.txt.enc`).
2.  **Verify** that the process was successful by decrypting the `secret_data.txt.enc` file to ensure you can recover the information with your password.
3.  **Delete** the original file (`secret_data.txt`) only after you have verified that the encrypted file is correct and accessible.
