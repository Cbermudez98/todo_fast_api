from bcrypt import gensalt, checkpw, hashpw

class Bcrypt():
    def __init__(self) -> None:
        self.salt = gensalt(rounds=10)
    
    def encrypt(self, pwd: str) -> str:
        bytes = pwd.encode("utf-8")
        return hashpw(bytes, self.salt).decode("utf-8")

    def compare(self, encrypted: str, password: str) -> bool:
        byte_pwd = password.encode("utf-8")
        byte_enc = encrypted.encode("utf-8")
        return checkpw(password=byte_pwd, hashed_password=byte_enc)