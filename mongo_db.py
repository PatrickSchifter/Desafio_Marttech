from pymongo import MongoClient


con_str = "mongodb+srv://user1:q4w3e2r1@testcluster.25rmd.mongodb.net/test"
client = MongoClient(con_str)

db = client.notebooks

collection_name = db["notebooks"]

