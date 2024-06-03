from ..errors.ApiKeyError import ApiKeyError
import os

'''
loads and checks the secret
useful because if someone someone gets hold of the API endpoint, they can make a tsunami of tweets
was lazy to implement it in the headers
TODO: add it in headers 
'''
class Secret:
    def __init__(self) -> None:
        self.SECRET = os.getenv("SECRET")
        if not self.SECRET:
            raise ApiKeyError("Missing Secret")
        
    def get(self) -> str:
        return self.SECRET