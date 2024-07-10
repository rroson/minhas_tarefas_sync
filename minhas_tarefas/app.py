from http import HTTPStatus
from fastapi import FastAPI
from minhas_tarefas.schemas import Mensagem
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", status_code=HTTPStatus.OK, response_model=Mensagem)
def read_root():
    return {'mensagem': 'Olá mundo!'}

@app.get("/html", response_class=HTMLResponse)
async def retorna_html(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})