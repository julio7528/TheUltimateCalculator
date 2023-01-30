#Importing Libraries
import os, traceback
from tkinter import messagebox

#Importing Modules
from log import logmessage as log

class Name:  
    """
    Description:
    Attributes:
    Methods:
    """      
    def __init__(self, n):
        self.n = n

    def ___privateExceution(self):
        pass
        return self.n

    def pubExcecution(self):
        pass
        return self.n

try:
    #call function pubExcetion
    def main():
        Name().pubExcecution()

except Exception as e:
    print(f"An Error Ocurred While Executing the File: {os.path.basename(__file__)} - Message: {e} - Line: {traceback.extract_tb(e.__traceback__)[0][1]}")
    log(f"An Error Ocurred While Executing the File: {os.path.basename(__file__)} - Message: {e} - Line: {traceback.extract_tb(e.__traceback__)[0][1]}")
    messagebox.showerror("Error",f"An Error Ocurred While Executing the File: {os.path.basename(__file__)}\nMessage: {e}\nLine: {traceback.extract_tb(e.__traceback__)[0][1]}")

