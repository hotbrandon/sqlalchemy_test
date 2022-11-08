from passlib import CryptoContext

pwd_context = CryptoContext(schemes=["bcrypt"], deprecated="auto")

class HashPassword:
    def create_hash(self, password: str):
        return pwd_context.hash(password)

    def verify_hash(self,password:str, hashed_password:str):
        return pwd_context.verify(password, hashed_password)
