"""
About:
    requirements.txt: File that contains all the dependencies of the project
    .gitignore: File that contains all the files that should not be uploaded to the repository
    .env: File that contains all the environment variables of the project (not in repository (use requirements.txt))
    The Database is recorded in an Azure SQL Server
"""
# Importing the libraries
import os, traceback, inspect
from tkinter import messagebox
from termcolor import colored

#Importing Modules
from modules.log import logmessage, logStruct
from modules.tree import treeRecord
from modules.jsonrec import jsonRecord
from calc import mainCalc
from modules.azureDB import insertTable

try:
    logStruct() #Record the structure of the project
    logmessage(f'Starting the project in File: {os.path.basename(__file__)}')
    n1, n2 = mainCalc()
    jsonRecord(n1, n2)
    insertTable(n1, n2)   
    treeRecord()    
except Exception as e:
    print(colored(f"🤣 🤣 🤣 An Error Ocurred While Executing the File: {os.path.basename(__file__)} - Message: {e} - Line: {traceback.extract_tb(e.__traceback__)[0][1]}", "red") + " \U0001F602" + " \U0001F602" + " \U0001F602")
    messagebox.showerror("Error",f"An Error Ocurred While Executing the File: {os.path.basename(__file__)}\nMessage: {e}\nLine: {traceback.extract_tb(e.__traceback__)[0][1]}")
    logmessage(f"An Error Ocurred While Executing the File: {os.path.basename(__file__)} - Message: {e} - Line: {traceback.extract_tb(e.__traceback__)[0][1]}")
finally:
    print()
    print("\033[1m- This is the end of the program\033[0m")
    logmessage(f"Program Finished - Line: {inspect.currentframe().f_lineno} - File: {os.path.basename(__file__)}")
    print("- For more information, check the log file " + (colored("./Logs/logStructure.txt", "blue")) + " in the project folder")
    print(f"- Check the tree file in ./Logs/treeStructure.txt" + "\U0001F600") 
    logStruct()
    delay = input(colored("Press any key to continue...", "green"))    
    os.system("cls")