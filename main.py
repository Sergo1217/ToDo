from fastapi import FastAPI, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from models.model import TaskDto
from services import service

templates = Jinja2Templates(directory="templates")
app = FastAPI()


@app.get("/")
async def home(req: Request):
    tasks = service.get_tasks()
    return templates.TemplateResponse("base.html", {"request": req, "tasks": tasks})


@app.post("/add")
def add(req: Request, task_data: TaskDto):
    service.add_task(task_data)
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)


@app.get("/delete/{task_id}")
def delete(req: Request, task_id: int):
    service.delete_task(task_id)
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)
