from fastapi.routing import APIRouter
from fastapi import status, HTTPException
from schemas import TodoGet, TodoPost, TodoPut
from models import Todo

router = APIRouter(prefix='/api/v1', tags=['Todos'])


@router.get('/')
async def all_todos():
    return await TodoGet.from_queryset(Todo.all())

async def post_todo(body: TodoPost):
    data = body.model_dump(exclude_unset=True)
    todo = await Todo.create(**data)
    return await TodoGet.from_tortoise_orm(todo)