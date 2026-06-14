
"""
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import psycopg2
import os
import time

app = FastAPI()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "tododb")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "secret")

def get_db_connection():
    for i in range(5):
        try:
            conn = psycopg2.connect(
                host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD
            )
            return conn
        except psycopg2.OperationalError:
            print("Database not ready yet, retrying in 2 seconds...")
            time.sleep(2)
    raise Exception("Could not connect to the database")

conn = get_db_connection()
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS todos (
      id SERIAL PRIMARY KEY,
      task TEXT NOT NULL
    );
""")
conn.commit()
cursor.close()
conn.close()

class TodoItem(BaseModel):
    task: str

@app.get('/', response_class=HTMLResponse)
def read_index():
    with open("src/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/api/todos")
def get_todos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT task FROM todos;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [row[0] for row in rows]

@app.post("/api/todos")
def add_todo(item: TodoItem):
    if not item.task.strip():
        raise HTTPException(status_code=400, detail="Task cannot be empty")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO todos (task) VALUES (%s);", (item.task,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"status": "success"}

@app.post("/api/todos/remove")
def remove_todo(item: TodoItem):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todos WHERE task = %s;", (item.task,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"status":"success"}
"""