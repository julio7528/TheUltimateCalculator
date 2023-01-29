# Importing the libraries
import os, traceback, json, inspect
from tkinter import messagebox

#Importing Modules
from modules.log import logmessage as log

class fJson:
    def __init__(self,a ,b):   
        self.a = a
        self.b = b  

    def __recordJson(self):
        with open("./InputOutput/output.json", "w") as file:
            log(f"Saving data in Json File - Line: {inspect.currentframe().f_lineno}")
            json.dump({"n1": self.a,
                        "n2": self.b,
                        "result": float(self.a/self.b)},
                        file,
                        indent=4,
                        ensure_ascii=False,
                        sort_keys=True
                        )
            log(f"Data Saved - Line: {inspect.currentframe().f_lineno}")

    def pubRecordJson(self):
        self.__recordJson()

def jsonRecord(a, b):
    fJson(a, b).pubRecordJson()

try:
    e = 0
except Exception as e:
    log(f"An Error Ocurred While Executing the File: {os.path.basename(__file__)} - Message: {e} - Line: {traceback.extract_tb(e.__traceback__)[0][1]}")
    messagebox.showerror("Error",f"An Error Ocurred While Executing the File: {os.path.basename(__file__)}\nMessage: {e}\nLine: {traceback.extract_tb(e.__traceback__)[0][1]}")