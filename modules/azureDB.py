#Importing Libraries
import pyodbc as pyo
import pandas as pd
import os, traceback, datetime
from tkinter import messagebox


#Importing Modules
from modules.log import logmessage as log
from modules.PassLoad import getPassword

class Name:   
    """
        This code provides a way to connect to an Azure database and close the connection. 
    Attributes: 
        n: None 
        pswDB: password for the database 
        cnn_azure: connection string for the Azure database 
        cnn: connection object for the Azure database 
        passW: password for the database 
        cn: connection object for the Azure database 
    Methods: 
        __getPsw(): gets the password from a secure source  
        psw(): returns the password from __getPsw()  
        connectDB(): establishes a connection to an Azure database using a provided password  
        closeDB(): closes an established connection to an Azure database
    """
    def __init__(self):
        self.n = None

    def __getPsw(self):
        psw = getPassword()
        return psw

    def psw(self):
        pswDB = self.__getPsw()
        return pswDB

    def connectDB(passW):
        cnn_azure = (
            r"Driver={SQL Server};Server=tcp:juliogomes.database.windows.net,1433"
            f".database.windows.net;Database=theUltimateCalculation;UID=juliogomes;PWD={passW}"
        )
        cnn = pyo.connect(cnn_azure)
        return cnn

    def closeDB(cn):
        cn.close()

try:
    """
    This module contains functions to create and insert data into a table in an Azure Database.
    Attributes: 
        pswDB (str): Password for the database. 
        n1 (int): First number to be used in the calculation. 
        n2 (int): Second number to be used in the calculation. 
        today (datetime): Current date and time. 
        date (str): Date formatted as YYYY-MM-DD. 
        result (float): Result of the calculation between n1 and n2. 
        comment (str): Comment about the calculation. 
    Methods: 
        createTable(pswDB = Name().psw()): Creates a table in an Azure Database with columns for date, n1, n2, result and comment. 
        insertTable(n1,n2,pswDB = Name().psw()): Inserts data into the table created by createTable() function with columns for date, n1, n2, result and comment.
    """
    def createTable(pswDB = Name().psw()):
        cn = Name.connectDB(pswDB)
        #Read .Database/createTable.sql file and record in a variable
        with open(".\DatabaseSQL\createTable.sql", "r") as file:
            sqlCreateTable = file.read()
        #Execute the SQL Query
        #print(sqlCreateTable)
        cursor = cn.cursor()
        cursor.execute(sqlCreateTable)
        cn.commit()
        Name.closeDB(cn)

    def insertTable(n1,n2,gptComment,pswDB = Name().psw()):
        createTable(pswDB)
        #Variables
        today = datetime.datetime.now()
        date = today.strftime("%Y-%m-%d")
        result = format(n1/n2, '.4f') 
        comment = gptComment       

        #execution:Read .Database/insertTable.sql file and record in a variable
        cn = Name.connectDB(pswDB)
        with open(".\DatabaseSQL\insertTable.sql", "r") as file:
            sqlInsertTable = file.read()
        cursor = cn.cursor()
        cursor.execute(sqlInsertTable, (date, n1, n2, result, comment))
        cn.commit()
        print()
        print(f"This Calculation was Recorded in Azure Database: {date}, {n1}, {n2}, {result}✅")
        log(f"Data Recorded in Azure Database: {date}, {n1}, {n2}, {result}")
        Name.closeDB(cn)

    def createTableAPI(pswDB = Name().psw()): #This function is used to create the table for the TwitterAPI
        cn = Name.connectDB(pswDB)
        #Read .Database/createTable.sql file and record in a variable
        with open(".\DatabaseSQL\createTableAPI.sql", "r") as file:
            sqlCreateTable = file.read()
        #Execute the SQL Query
        #print(sqlCreateTable)
        cursor = cn.cursor()
        cursor.execute(sqlCreateTable)
        cn.commit()
        Name.closeDB(cn)

except Exception as e:
    print(f"An Error Ocurred While Executing the File: {os.path.basename(__file__)} - Message: {e} - Line: {traceback.extract_tb(e.__traceback__)[0][1]}")
    log(f"An Error Ocurred While Executing the File: {os.path.basename(__file__)} - Message: {e} - Line: {traceback.extract_tb(e.__traceback__)[0][1]}")
    messagebox.showerror("Error",f"An Error Ocurred While Executing the File: {os.path.basename(__file__)}\nMessage: {e}\nLine: {traceback.extract_tb(e.__traceback__)[0][1]}")

