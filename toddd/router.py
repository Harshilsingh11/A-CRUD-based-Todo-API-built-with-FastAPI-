from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.db import get_db
from toddd.dtos import UserSchema, TodoSchema
from toddd.controller import *
from utils.helper import *
from utils.authController import login,register
#  (
#     getUser, getTodosByUser, createUser, updateUser, deleteUser,
#     getTodos, createTodo, updateTodo, deleteTodo
# )



userRouter = APIRouter(prefix="/users")
todoRouter = APIRouter(prefix="/todos")



# @userRouter.get("/")
# def fetch_users(db: Session = Depends(get_db)):
#     return getUser(db)

# @userRouter.get("/{id}")
# def fetch_user(id: int, db: Session = Depends(get_db)):
#     return getUser(db, id)

# @userRouter.get("/{id}/todos")
# def fetch_user_todos(id: int, db: Session = Depends(get_db)):
#     return getTodosByUser(id, db)

# @userRouter.post("/")
# def add_user(body: UserSchema, db: Session = Depends(get_db)):
#     return createUser(body, db)

# @userRouter.put("/{id}")
# def modify_user(id: int, body: UserSchema, db: Session = Depends(get_db)):
#     return updateUser(id, body, db)

# @userRouter.delete("/{id}")
# def remove_user(id: int, db: Session = Depends(get_db)):
#     return deleteUser(id, db)

# @todoRouter.get("/")
# def fetch_todos(db: Session = Depends(get_db)):
#     return getTodos(db)

# @todoRouter.get("/{id}")
# def fetch_todo(id: int, db: Session = Depends(get_db)):
#     return getTodos(db, id)

# @todoRouter.post("/user/{user_id}")
# def add_todo(user_id: int, body: TodoSchema, db: Session = Depends(get_db)):
#     return createTodo(body, user_id, db)

# @todoRouter.put("/{id}")
# def modify_todo(id: int, body: TodoSchema, db: Session = Depends(get_db)):
#     return updateTodo(id, body, db)

# @todoRouter.delete("/{id}")
# def remove_todo(id: int, db: Session = Depends(get_db)):
#     return deleteTodo(id, db)

@userRouter.get("/")
def fetchUser(db:Session =Depends(get_db),user:User = Depends(is_authinticated)):
    return getUser(db,user)


@userRouter.get("/all")
def all_users(db: Session = Depends(get_db)):
    return getAllUsers(db)
# @userRouter.get("/")
# def fetch_user_todos(user:User =Depends(is_authinticated) , db: Session = Depends(get_db)):
#     return getTodosByUser(user, db)

@userRouter.get("/")
def fetch_user_todos(id: int, db: Session = Depends(get_db)):
    return getTodosByUser(id, db)

@userRouter.post("/register")
def add_user(body: UserSchema, db: Session = Depends(get_db)):
    return register(body, db)

@userRouter.post("/login")
def loginn(body:LoginSchema, db:Session = Depends(get_db)):
    return login(body, db)

@userRouter.put("/")
def modify_user( body: UserSchema,user:User=Depends(is_authinticated) , db: Session = Depends(get_db)):
    return updateUser(user, body, db)

@userRouter.delete("/")
def remove_user(user:User = Depends(is_authinticated), db: Session = Depends(get_db)):
    return deleteUser(user, db)

@todoRouter.get("/")
def fetch_user_todo(user:User =Depends(is_authinticated),db:Session = Depends(get_db)):
    return getTodosByUser(user,db)
 
@todoRouter.get("/all")
def fetch_all_todo( db:Session = Depends(get_db)):
    return getalltodos(db)

@todoRouter.post("/")
def add_todo( body: TodoSchema,user: User=Depends(is_authinticated), db: Session = Depends(get_db)):
    return createTodo(body, user, db)

@todoRouter.put("/")
def modify_todo(body: TodoSchema,user:User=Depends(is_authinticated),  db: Session = Depends(get_db)):
    return updateTodo(user, body, db)

@todoRouter.delete("/")
def remove_todo(user:User=Depends(is_authinticated), db: Session = Depends(get_db)):
    return deleteTodo(user, db)