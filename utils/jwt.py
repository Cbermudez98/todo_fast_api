from jwt import encode, decode

from config.environments import parameter_store

class Jwt():
    def __init__(self):
        self.secret = parameter_store["JWT_KEY"]
        self.algorithm = parameter_store["JWT_ALGORITHM"]
    
    def encode(self, payload: dict) -> str:
        return encode(payload=payload, algorithm=self.algorithm, key=self.secret)
    
