from http import HTTPStatus
from fastapi import FastAPI
from minhas_tarefas.schemas import Mensagem, UsuarioSchema, UsuarioPublic, UsuarioDB, UsuarioList
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
database = [] #Fake Database

@app.get("/", status_code=HTTPStatus.OK, response_model=Mensagem)
def read_root():
    return {'mensagem': 'Olá mundo!'}

@app.get("/html/", response_class=HTMLResponse)
async def retorna_html(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UsuarioPublic)
def create_user(usuario: UsuarioSchema):
    usuario_id = UsuarioDB(
        id=len(database) + 1,
        **usuario.model_dump() # Altera o objeto UsuarioSchema para Dicionário
    )
    database.append(usuario_id)
    return usuario_id

@app.get('/users/', response_model=UsuarioList)
def read_users():
    return {'users': database}