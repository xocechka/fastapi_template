import imp

from fastapi import APIRouter
from security.auth.router import auth_router

from .endpoints import person

app_router = APIRouter()


# Endpoints

# Auth
app_router.include_router(auth_router)

# Resources
app_router.include_router(person.router)
