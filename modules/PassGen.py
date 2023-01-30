#Importing Libraries
import os, traceback
from tkinter import messagebox
from cryptography.fernet import Fernet

#Importing Modules
from log import logmessage as log

class CreatePass:
    """
        Description: 
            This class is used to generate a new password by encrypting it with a key. 
            In GitHub Don't Save the Key, but in the local repository it is saved.
        Attributes: 
            self.key (str): The key used for encryption. 

        Methods: 
            __create_key(): Generates a new key for encryption. 
            __save_key(): Saves the generated key in a file. 
            __set_secret_key(): Encrypts the new password with the generated key.  
            __open_secret_key(): Saves the encrypted password in a file.  
            __decrypt_secret_key(): Decrypts the encrypted password using the generated key.  
            pubPassGenerator(): Generates and saves a new encrypted password.  
    """  
    def __init__(self):
        self.key = None

    def __create_key(self):
        self.key = Fernet.generate_key()
        return  self.key

    def __save_key(self):
        with open("./modules/keyCalculation.key", "wb") as key_file:
            key_file.write(self.key)
            return "./modules/keyCalculation.key"

    def __set_secret_key(self):
        cipher_suite = Fernet(self.key)
        newPass = input("Enter the password: ").encode()
        cipher_text = cipher_suite.encrypt(newPass)
        return cipher_text, cipher_suite

    def __open_secret_key(self, cipher_text):
        with open("./modules/newKeyCalculation.key", "wb") as key_file:
            key_file.write(cipher_text)

    def __decrypt_secret_key(self, cipher_text, cipher_suite):
        plain_text = cipher_suite.decrypt(cipher_text)
        print("Password Convert Successfully")
        return plain_text

    def pubPassGenerator(self):
        print("Task to Insert New Password")
        print()
        key = self.__create_key()
        print(f"Key Compile Generated: {key}")
        pathKey = self.__save_key()
        print(f"Key Saved: {pathKey}")
        print()
        calcKey, suiteKey = self.__set_secret_key()
        print()
        print(f"Key Calculated: {calcKey}")
        self.__open_secret_key(calcKey)
        print(f"Calculated Key Saved: {calcKey}")
        return self.__decrypt_secret_key(calcKey, suiteKey)
try:
    os.system("cls")
    keypassword = CreatePass().pubPassGenerator()
    keypassword = keypassword.decode()
    input("Press any key to continue...")
    os.system("cls")
    log(f"Password Changed Successfully - File: {os.path.basename(__file__)}")
except Exception as e:
    print(f"An Error Ocurred While Executing the File: {os.path.basename(__file__)} - Message: {e} - Line: {traceback.extract_tb(e.__traceback__)[0][1]}")
    log(f"An Error Ocurred While Executing the File: {os.path.basename(__file__)} - Message: {e} - Line: {traceback.extract_tb(e.__traceback__)[0][1]}")
    messagebox.showerror("Error",f"An Error Ocurred While Executing the File: {os.path.basename(__file__)}\nMessage: {e}\nLine: {traceback.extract_tb(e.__traceback__)[0][1]}")

# # Gera a chave
# key = Fernet.generate_key()
# print(key)

# # Armazena a chave em um arquivo
# with open("secret0.key", "wb") as key_file:
#     key_file.write(key)

# # Lê a chave do arquivo
# with open("secret0.key", "rb") as key_file:
#     key = key_file.read()
#     print(key)

# # Cifra o texto
# cipher_suite = Fernet(key)
# cipher_text = cipher_suite.encrypt(b"secret message")
# print(cipher_text)

# # Armazena o texto em um arquivo
# with open("secret.key", "wb") as key_file:
#     key_file.write(cipher_text)

# # Lê o texto do arquivo
# with open("secret.key", "rb") as key_file:
#     cipher_text = key_file.read()

# # Decifra o texto
# plain_text = cipher_suite.decrypt(cipher_text)

# print(plain_text)
#***********************************************************************

# Lê a chave do arquivo
# with open("secret0.key", "rb") as key_file:
#     key = key_file.read()
#     print(key)

# cipher_suite = Fernet(key)

# # Lê o texto do arquivo
# with open("secret.key", "rb") as key_file:
#     cipher_text = key_file.read()

# # Decifra o texto
# plain_text = cipher_suite.decrypt(cipher_text)

# print(plain_text)