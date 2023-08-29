from dotenv import load_dotenv
import os

load_dotenv()

class Constants :

    def getToken():
        token = "TOKEN"
        print(os.getenv(token))
        return os.getenv(token)

    def getKey():
        key = "KEY"
        return os.getenv(key)


