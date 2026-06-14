from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

origins = [
    "http://localhost:4200",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

todo_list = ["Kupić mleko", "Skonfigurować Postgresa", "Napisać testy"]

class Task(BaseModel):
    task: str

@app.get("/api/data")
def get_data():
    return todo_list

@app.post("/api/tasks")
def create_task(payload: Task):
    todo_list.append(payload.task)
    return todo_list

@app.delete("/api/tasks/{task_id}")
def delete_task(task_id: int):
    if 0 <= task_id < len(todo_list):
        todo_list.pop(task_id)
        return todo_list
    raise HTTPException(status_code=404, detail="Task not found")