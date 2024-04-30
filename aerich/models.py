from fastapi import FastAPI
#from api.routing import router as todo_router
from fastapi.routing import APIRouter
from tortoise.contrib.fastapi import register_tortoise
#from settings.configuration import Config
from typing import List



class Config:
    DB_MODELS:List[str] = ['api.models']


todo_router = APIRouter(prefix='/api/v1', tags=['Todos'])


app = FastAPI()
app.include_router(todo_router)

register_tortoise(
    app=app,
    db_url='mysql://root:@127.0.0.1:3307/todo',
    modules={'models': Config.DB_MODELS},
    add_exception_handlers=True,
    generate_schemas=False
)

@app.get('/')

def home ():
    return "MINI-PROJET TO DO LIST ...!"