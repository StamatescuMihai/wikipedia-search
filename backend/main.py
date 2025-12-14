from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.search_router import router as search_router
from backend.database.connection import init_db

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

app.include_router(search_router)
