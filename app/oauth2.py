from jose import JWTError,jwt
from datetime import datetime, timedelta

 #SECREtT_KEY
 #Algorithm 
 #Expriation time

SECRET_KEY =  "07dvj56987nerty0789236dj06vncei9013weskutdnnfecs3657jkesaec2"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRT_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRT_MINUTES) 
    to_encode.update({"exp": expire}) 

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

