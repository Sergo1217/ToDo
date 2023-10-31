from fastapi import Depends, FastAPI, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from models.model import TaskDto
from models.orm import get_db
from services import service

templates = Jinja2Templates(directory="templates")
app = FastAPI()


@app.get("/")
async def home(req: Request, db: Session = Depends(get_db)):
    tasks = service.get_tasks(db)
    return templates.TemplateResponse("base.html", {"request": req, "tasks": tasks})


@app.post("/add")
def add(req: Request, task_data: TaskDto, db: Session = Depends(get_db)):
    service.add_task(db, task_data)
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)


@app.get("/delete/{task_id}")
def delete(req: Request, task_id: int, db: Session = Depends(get_db)):
    service.delete_task(db, task_id)
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)
