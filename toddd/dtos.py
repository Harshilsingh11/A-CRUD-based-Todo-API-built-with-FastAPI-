from typing import Literal
from pydantic import BaseModel
from datetime import date
  
class UserSchema(BaseModel):
    name : str | None=None
    email : str
    username : str 
    mobile: int | None=None


class TodoSchema(BaseModel):
    title: str
    description: str | None = None
    priority: Literal["low", "medium", "high"]  | None=None
    completed: bool = False
    start_date: date | None=None
    end_date: date | None=None

class LoginSchema(BaseModel):
    username:str
    password:str    