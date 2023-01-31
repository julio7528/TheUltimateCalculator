#Importing Libraries
import os, traceback, tweepy, openai
from tkinter import messagebox

#Importing Modules
from modules.log import logmessage as log
from modules.azureDB import Name

class GetApiData:  
    """
    This class is used to select data from the TwitterDatabaseApi.
    Methods: 
        __SelectDataAPI(): Connects to the TwitterDatabaseApi and fetches the Api_Key, Api_Secret_Key, Access_Token, and Access_Token_Secret. 
        pubSelctDataAPI(): Returns the values fetched by __SelectDataAPI(). 
    """   
    def __init__(self):
        self.n = None

    def __SelectDataGPTAPI(self):
        azPsw = Name().psw()
        cnn = Name.connectDB(azPsw)
        cursor = cnn.cursor()
        cursor.execute("SELECT Api_Key FROM ChatGPTDatabaseApi;")
        row = cursor.fetchone()
        Api_Key = row[0]
        cnn.commit()
        Name.closeDB(cnn)             
        return Api_Key

    def __SelectDataAPITwitter(self):
        azPsw = Name().psw()
        cnn = Name.connectDB(azPsw)
        cursor = cnn.cursor()
        cursor.execute("SELECT Api_Key, Api_Secret_Key, Access_Token, Access_Token_Secret FROM TwitterDatabaseApi;")
        row = cursor.fetchone()
        Api_Key = row[0]
        Api_Secret_Key = row[1]
        Access_Token = row[2]
        Access_Token_Secret = row[3]
        cnn.commit()
        Name.closeDB(cnn)             
        return Api_Key, Api_Secret_Key, Access_Token, Access_Token_Secret

    def pubSelctDataAPITwitter(self):
        return self.__SelectDataAPITwitter()

    def pubSelctDataAPIGPT(self):
        return self.__SelectDataGPTAPI()
try: 
    def selctDataChatGPTApi(n1,n2):
        Api_Key = GetApiData().pubSelctDataAPIGPT()
        openai.api_key = Api_Key
        model_engine = "text-davinci-003"
        prompt = f"Please Explain in 256 Characters the Division Between {n1} and {n2} and your float answer"
        # Generate a response
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        response = completion.choices[0].text
        print(f"\nOur ChatGPT Specialist Comment: {response}")
        return response
        
    def SelctDataTwAPI(message):
        #call function pubSelctDataAPI
        Api_Key, Api_Secret_Key, Access_Token, Access_Token_Secret = GetApiData().pubSelctDataAPITwitter()
        #Conncetion to Twitter API
        auth = tweepy.OAuthHandler(Api_Key, Api_Secret_Key)
        auth.set_access_token(Access_Token, Access_Token_Secret)
        api = tweepy.API(auth)        
        #Send Tweet
        print("The result of Calculation With Comments is Succesful Posted in Twitter Account: @JavierG19128531")
        api.update_status(message)
        return message

    def mainApi(n1,n2):
        gptAnswer = SelctDataTwAPI(selctDataChatGPTApi(n1,n2))
        return gptAnswer

except Exception as e:
    print(f"An Error Ocurred While Executing the File: {os.path.basename(__file__)} - Message: {e} - Line: {traceback.extract_tb(e.__traceback__)[0][1]}")
    log(f"An Error Ocurred While Executing the File: {os.path.basename(__file__)} - Message: {e} - Line: {traceback.extract_tb(e.__traceback__)[0][1]}")
    messagebox.showerror("Error",f"An Error Ocurred While Executing the File: {os.path.basename(__file__)}\nMessage: {e}\nLine: {traceback.extract_tb(e.__traceback__)[0][1]}")


