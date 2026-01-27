from fastapi import FastAPI
from app.models import User
from .database import create_db_and_tables, get_session
app = FastAPI()


@app.get('/')
def hello_world():
    return "Hello, World!"

