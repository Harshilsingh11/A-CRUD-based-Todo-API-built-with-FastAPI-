from fastapi import Request,HTTPException,status,Depends
import jwt
from sqlalchemy.orm import Session
from utils.db import get_db
from utils.authController import SECRET_KEY ,ALGORITHM , get_User_by_username
def is_authinticated(req:Request , db:Session = Depends(get_db)):
    try:
        token = req.headers.get("authorization")
        if not token:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED,detail={"error":"your not authorised"})
        token=token.split(" ")[-1]
        data=jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        if not data.get("username"):
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail={"error":"you are not authorised"})
        user = get_User_by_username(data.get("username"),db)
        if not user:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail={"error":"you are not authorised"})
        
        return user
    except:
       raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail={"error":"you are not authorised"})





##date wise filter 
