from fastapi import FastAPI
from app.api.routes_users import router as users_router

app = FastAPI(title="FastAPI Mongo Example")

app.include_router(users_router)

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI + MongoDB project!"}
