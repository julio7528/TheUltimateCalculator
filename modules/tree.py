"""
This module contains the 'tree' class and the treeRecord function.

Class tree: 
    tFile (str): Path to Tree.txt file. 
    tCommand (str): Output of the command "tree /f". 
    __record(self): Writes the output of tCommand to tFile. 
    pubRecord(self): Calls __record() to write the output of tCommand to tFile. 

Function treeRecord(): Calls pubRecord() from the tree class to write the output of tCommand to tFile. Catches any exceptions with ErrorHandling(). 
"""
# Importing the libraries
import io, subprocess, os, traceback
from tkinter import messagebox

#Importing Modules
from modules.log import logmessage as log

class tree:
    def __init__(self):   
        self.tFile = './modules/Tree.txt'
        self.tCommand = subprocess.getoutput("tree /f")        

    def __record(self): #Record the current tree structure of the project
        with io.open(self.tFile, 'a+', encoding="utf-8") as file:
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