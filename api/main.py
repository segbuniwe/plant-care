from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from authenticator import authenticator
from routers import accounts, favorites, plants

app = FastAPI()

app.include_router(accounts.router, tags=["accounts"])
app.include_router(authenticator.router, tags=["accounts"])
app.include_router(favorites.router, tags=["favorites"])
app.include_router(plants.router, tags=["plants"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("CORS_HOST", "http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
