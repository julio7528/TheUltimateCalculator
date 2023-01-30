# Importing the libraries
import io, subprocess, os, traceback
from tkinter import messagebox

#Importing Modules
from modules.log import logmessage as log
class tree:
    
    """
    This class is used to record the tree structure of the project. 
    Attributes: 
    tFile (str): Path to the file where the tree structure will be stored. 
    tCommand (subprocess): Command used to get the tree structure of the project. 
    Methods: 
    __record(): Private method used to record the current tree structure of the project in tFile. 
    pubRecord(): Public method that calls __record() to record the current tree structure of the project. 
    """
    
    def __init__(self):   
        self.tFile = './Logs/Tree.txt'
        self.tCommand = subprocess.getoutput("tree /f")        

    def __record(self): #Record the current tree structure of the project
        with io.open(self.tFile, 'w', encoding="utf-8") as file:
            file.write(self.tCommand)            
            log(f'Tree Structure Recorded in {self.tFile} encodec as utf-8')
        file.close()

    def pubRecord(self):
        self.__record()

def treeRecord():
    tree().pubRecord()

try:
    e = 0
except Exception as e:
    log(f"An Error Ocurred While Executing the File: {os.path.basename(__file__)} - Message: {e} - Line: {traceback.extract_tb(e.__traceback__)[0][1]}")
    messagebox.showerror("Error",f"An Error Ocurred While Executing the File: {os.path.basename(__file__)}\nMessage: {e}\nLine: {traceback.extract_tb(e.__traceback__)[0][1]}")