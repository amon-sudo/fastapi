import re
from typing import List
from urllib import response

from dns import query
from fastapi import FastAPI, Depends, status, Response, HTTPException
from sentry_sdk import session

from blog.routers import user

from . import schemas,  models, hashing
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from .routers import blog, user, authentication

from .database import engine, sessionLocal, get_db


app = FastAPI()


models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)