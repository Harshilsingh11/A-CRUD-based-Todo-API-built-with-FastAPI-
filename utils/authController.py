from datetime import datetime, timedelta, timezone
from typing import Annotated
from sqlalchemy.orm import Session
from toddd.model import User

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from pydantic import BaseModel
from toddd.dtos import  LoginSchema ,UserSchema


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_User_by_username(username:str,db:Session):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return None
    
    return user



def register(body:UserSchema,db:Session):
   currentuser = get_User_by_username(body.username,db)
   if currentuser:
       raise HTTPException(409, detail={"error":"User alredy exist for this username"})
   
   hp = get_password_hash(body.password)

   newUser = User(username= body.username, 
                  hass_password=hp, 
                  email = body.email, 
                  name=body.name)
   db.add(newUser)
   db.commit()
   db.refresh(newUser)

   return {"Done":newUser , "status":"User Registerred Successfuly..."}


def login(body:LoginSchema,db:Session):
    currentuser = get_User_by_username(body.username,db)
    if not currentuser:
        raise HTTPException(404, detail={"error":"user not found"})
    
    varifyPass = verify_password(body.password,currentuser.hass_password)

    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    token = jwt.encode({"username":currentuser.username,"exp":expire},SECRET_KEY,algorithm=ALGORITHM)

    return{"token":token , "message":"You loggedin sucessfull"}