from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

todos = ["Buy milk", "Run Docker", "Configure Nginx"]

class TodoItem(BaseModel):
    task: str

@app.get("/", response_class=HTMLResponse)
def read_index():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/api/todos")
def get_todos():
    return todos

@app.post("/api/todos")
def add_todo(item: TodoItem):
    if not item.task.strip():
        raise HTTPException(status_code=400, detail="Task can't be null")
    todos.append(item.task)
    return {"status": "success"}

@app.post("/api/todos/remove")
def remove_todo(item: TodoItem):
    if item.task in todos:
        todos.remove(item.task)
        return {"status": "success"}
    raise HTTPException(status_code=404, detail="No task found")