from mongo_db import collection_name
from bson import ObjectId


def notebook_serializer(notebook) -> dict:
    return {
        "id": str(notebook["_id"]),
        "name": notebook["name"],
        "description": notebook["description"],
    }


def notebooks_serializer(notebooks) -> list:
    return [notebook_serializer(notebook) for notebook in notebooks]


def update_notebook(id, anotations):
    notebook = notebooks_serializer(collection_name.find({"_id": ObjectId(id)}))
    info = {"$set": {
                "anotations.$": [
                    {
                        "titulo": anotations.titulo,
                        "date_creation": anotations.data_criacao,
                        "lst_mod": anotations.data_mod,
                        "tags": anotations.tags
                    }
                ]
            }
        }
    return info
