from fastapi import FastAPI
from app.routes.machine_learning_routes import todo_api_router

app = FastAPI()

app.include_router(todo_api_router)
