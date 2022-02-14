from fastapi import FastAPI
from routes import notebook_api_router

app = FastAPI()

app.include_router(notebook_api_router)
