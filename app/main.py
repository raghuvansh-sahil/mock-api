from fastapi import FastAPI
from database import Startup, initialise_database, insert_startup_inDB, get_startups_fromDB

app = FastAPI()

@app.on_event("startup")
def on_startup():
    initialise_database()

@app.post("/insert-startup")
def insert_startup(startup: Startup):
    insert_startup_inDB(startup)
    return {"message": "Startup inserted successfully"}

@app.get('/get-startups')
def get_startups():
    return get_startups_fromDB()