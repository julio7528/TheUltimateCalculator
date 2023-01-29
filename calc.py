#Importing Libraries
import inspect, json, os, traceback
from tkinter import messagebox
from termcolor import colored

#Importing Modules
from modules.log import logmessage as log

class calculateDiv:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __division(self):
        log(f"Division of {self.a} and {self.b} - Line: {inspect.currentframe().f_lineno} - File: {os.path.basename(__file__)}")
        self.c = self.a/self.b
        return self.c

    def __evaluateResult(self):
        self.c = self.__division()        
        if type(self.c) == float:
            log(f"Result is Float: {format(float(self.c), '.4f')} - Line: {inspect.currentframe().f_lineno} - File: {os.path.basename(__file__)}")        
            return f"Float: {format(float(self.c), '.4f')}"        
        elif type(self.c) == int:
            log(f"Result is Integer: {int(self.c)} - Line: {inspect.currentframe().f_lineno} - File: {os.path.basename(__file__)}")
            return f"Integer: {int(self.c)}"

    #Input Session
    def __inputTwoNumbers(self):
        # a = int(input("Type a number: "))
        # b = int(input("Type another number: "))
        log(f"Reading Json File - Line: {inspect.currentframe().f_lineno} - File: {os.path.basename(__file__)}")
        with open("./InputOutput/input.json", "r") as file:
            data = json.load(file)
            self.a = data["n1"]
            self.b = data["n2"]
            log(f"First Number Charged From Json File: {self.a} - Line: {inspect.currentframe().f_lineno} - File: {os.path.basename(__file__)}")
            vYellowA = colored(f" {self.a}", "yellow")
            print(f"First Number Charged From Json File: {vYellowA}")
            log(f"Second Number Charged From Json File: {self.b} - Line: {inspect.currentframe().f_lineno} - File: {os.path.basename(__file__)}")
            vYellowB = colored(f" {self.b}", "yellow")
            print(f"Second Number Charged From Json File: {vYellowB}")
        if self.b == 0:
            log(f"Division by zero - Line: {inspect.currentframe().f_lineno} - File: {os.path.basename(__file__)}")
            raise ZeroDivisionError("Cannot divide by zero") #Raaise the error and stop the program
        return self.a, self.b
    

    def pubDivision(self, a, b):
        self.__division()
        return self.c

    def pubEvaluateResult(self):
        self.__evaluateResult()
        return format(float(self.c), '.4f')

    def pubInputTwoNumbers(self):
        self.__inputTwoNumbers()
        return self.a, self.b

try:
    #call function pubEvaluateResult and print result
    def mainCalc():
        n1,n2 = (calculateDiv(0,0).pubInputTwoNumbers())
        vBlue = colored(f" {(calculateDiv(n1,n2).pubEvaluateResult())}", "blue")
        vBlue = "\033[1m" + vBlue + "\033[1m"
        print(f'The Result of Division: {vBlue}')
        return n1,n2

except Exception as e:
    print(f"An Error Ocurred While Executing the File: {os.path.basename(__file__)} - Message: {e} - Line: {traceback.extract_tb(e.__traceback__)[0][1]}")
    log(f"An Error Ocurred While Executing the File: {os.path.basename(__file__)} - Message: {e} - Line: {traceback.extract_tb(e.__traceback__)[0][1]}")
    messagebox.showerror("Error",f"An Error Ocurred While Executing the File: {os.path.basename(__file__)}\nMessage: {e}\nLine: {traceback.extract_tb(e.__traceback__)[0][1]}")

