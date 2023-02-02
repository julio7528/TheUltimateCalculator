#Importing Libraries
import os, traceback, smtplib
from tkinter import messagebox

#Importing Modules
from modules.log import logmessage as log
from modules.azureDB import Name

class MailService:
    """
        This class provides a Gmail service.

        Attributes:
        n - a private attribute to store data.

        Methods:
        ___gmailConnection() - Establishes a connection to the Gmail database and returns the user and key information. 
        pubExcecution() - Returns a dictionary with the user and key information. 
    """    
    def __init__(self):
        self.n = None

    def ___MailConnection(self):
        azPsw = Name().psw()
        cnn = Name.connectDB(azPsw)
        cursor = cnn.cursor()
        cursor.execute("SELECT * FROM vaultGmail;")
        row = cursor.fetchone()
        waKey = row[1]
        waUser = row[2]        
        cnn.commit()
        Name.closeDB(cnn)                    
        return waKey, waUser

    def pubExcecution(self):
        waKey, waUser = self.___MailConnection()
        dictGmail = {
        "vSender": waUser,
        "vPassword": waKey
        }
        return dictGmail

try:
    #call function pubExcetion
    def getMailAccess():
        dictMail = MailService().pubExcecution()
        return dictMail

    def sendEmail(dictMail, n1, n2, gptComment):
        vIdList = [dictMail["vSender"], dictMail["vSender"], dictMail["vPassword"]]

        subject = f"Result from {n1} and {n2}."
        body = f"Subject: Result from {n1} and {n2} - Here is the result of division between \n\n{n1} and {n2} following the GP3 IA Comment:\n\n{gptComment}. \n The comment Result is in @JavierG19128531"
        message = f"Subject: {subject}\n\n{body}"
        with smtplib.SMTP_SSL("mail.pointec.dev", 465) as server:
            server.login(vIdList[0], vIdList[2])
            server.sendmail(vIdList[0], vIdList[0], message)
        print(f"Email/Report of Calculation -  Sent to : {vIdList[0]}, Subject: {subject} ✅")
        log(f"Email Sent to : {vIdList[0]}, Subject: {subject}")

except Exception as e:
    print(f"An Error Ocurred While Executing the File: {os.path.basename(__file__)} - Message: {e} - Line: {traceback.extract_tb(e.__traceback__)[0][1]}")
    log(f"An Error Ocurred While Executing the File: {os.path.basename(__file__)} - Message: {e} - Line: {traceback.extract_tb(e.__traceback__)[0][1]}")
    messagebox.showerror("Error",f"An Error Ocurred While Executing the File: {os.path.basename(__file__)}\nMessage: {e}\nLine: {traceback.extract_tb(e.__traceback__)[0][1]}")

