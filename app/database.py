import sqlite3
from pydantic import BaseModel

class Startup(BaseModel):
    startup_name: str
    tagline: str
    description: str

def initialise_database():
    connection = sqlite3.connect('startups.db')
    cursor = connection.cursor()
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS startups (
            startup_name TEXT,
            tagline TEXT,
            description TEXT
        )
    ''')
    connection.commit()

def insert_startup_inDB(startup: Startup):
    connection = sqlite3.connect('startups.db')
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO startups (startup_name, tagline, description)
        VALUES (?, ?, ?)
    ''', (startup.startup_name, startup.tagline, startup.description))
    connection.commit()
    print("Startup successfully saved to the database.")

def get_startups_fromDB():
    startups = []
    connection = sqlite3.connect('startups.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM startups')
    table = cursor.fetchall()
    if table:
        for row in table:
            startup = {
                "startup_name": row[0],
                "tagline": row[1],
                "description": row[2],
            }
            startups.append(startup)
    return startups