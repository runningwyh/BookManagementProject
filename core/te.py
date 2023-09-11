#-*- coding: UTF-8 -*-
from jose import JWTError, jwt

from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi import FastAPI
from core.config import SECRET_KEY, ALGORITHM


app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl=TOKEN_URL)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="dev-api/auth/token")


# 验证密码
async def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# 密码加密
async def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
