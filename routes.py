from fastapi import APIRouter
from mongo_db import collection_name
from models import Notebook, Anotations
from schema import notebook_serializer, notebooks_serializer, update_notebook
from bson import ObjectId

notebook_api_router = APIRouter()


@notebook_api_router.get("/")
async def get_notebooks():
    notebooks = notebooks_serializer(collection_name.find())
    return {"status": "ok", "data": notebooks}


@notebook_api_router.get("/{id}")
async def get_notebook(id: str):
    notebook = notebooks_serializer(collection_name.find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": notebook}


@notebook_api_router.post("/")
async def create_notebook(notebook: Notebook):
    _id = collection_name.insert_one(dict(notebook))
    notebook = notebooks_serializer(collection_name.find({"_id": _id.inserted_id}))
    return {"status": "Notebook added", "data": notebook}


@notebook_api_router.post("/{id}")
async def create_anotation(id: str, anotation : Anotations):
    collection_name.update({"_id": id}, update_notebook(id, anotation))
    return {"status": "Anotation added", "notes": notebooks_serializer(collection_name.find({"_id": id}))}
