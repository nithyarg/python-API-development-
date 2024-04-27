from passlib.context import CryptContext
pwd_Context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(passward: str):
    return pwd_Context.hash(passward) 

def verify(plain_password, hashed_password):
    return pwd_Context.verify(plain_password, hashed_password)