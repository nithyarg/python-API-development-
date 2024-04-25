from passlib.context import CryptContext
pwd_Context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(passward: str):
    return pwd_Context.hash(passward) 