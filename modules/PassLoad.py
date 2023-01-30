#Importing Libraries
import os, traceback
from tkinter import messagebox
from cryptography.fernet import Fernet

#Importing Modules
from modules.log import logmessage as log

class CreatePass:
    """
        This class is used to get a public pass.
    Attributes: 
        key (str): Stores the key of the file. 
    Methods: 
        __create_key(): Reads the key of the file and returns the plain text. 
        pubPassGenerator(): Generates a public pass. 
    """
    def __init__(self):
        self.key = None

    def __create_key(self):
        #Read Key of File
        with open("./modules/keyCalculation.key", "rb") as key_file:
            key = key_file.read()
        #Return Key Convert
        cipher_suite = Fernet(key)
        #Open Key Calculated
        with open("./modules/newKeyCalculation.key", "rb") as key_file:
            cipher_text = key_file.read()
        ###
        plain_text = cipher_suite.decrypt(cipher_text)
        return plain_text

    def pubPassGenerator(self):
        return self.__create_key()        
try:
    def getPassword():
        dbPassWord = CreatePass().pubPassGenerator()
        if dbPassWord is not None:
            dbPassWord = str(dbPassWord.decode())
            log(f"Password Loaded Successfully - File: {os.path.basename(__file__)}")
        else:
            print("No password generated")
            log(f"ERROR: No password generated - Check Problem of Password not generated or key file not found. - File: {os.path.basename(__file__)}")
            raise Exception("No password generated - Check Problem of Password not generated or key file not found.")            
        return dbPassWord
    
except Exception as e:
    print(f"An Error Ocurred While Executing the File: {os.path.basename(__file__)} - Message: {e} - Line: {traceback.extract_tb(e.__traceback__)[0][1]}")
    log(f"An Error Ocurred While Executing the File: {os.path.basename(__file__)} - Message: {e} - Line: {traceback.extract_tb(e.__traceback__)[0][1]}")
    messagebox.showerror("Error",f"An Error Ocurred While Executing the File: {os.path.basename(__file__)}\nMessage: {e}\nLine: {traceback.extract_tb(e.__traceback__)[0][1]}")
