from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from minhas_tarefas.schemas import Mensagem, UsuarioSchema, UsuarioPublic, UsuarioDB, UsuarioList
from minhas_tarefas.settings import Settings
from minhas_tarefas.database import get_session
from minhas_tarefas.models import Usuario


app = FastAPI()
# database = [] #Fake Database

@app.get("/", status_code=HTTPStatus.OK, response_model=Mensagem)
def read_root():
    return {'mensagem': 'Olá mundo!'}

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UsuarioPublic)
def create_user(usuario: UsuarioSchema, session: Session = Depends(get_session)):
    db_user = session.scalar(
        select(Usuario).where(
            Usuario.usuario == usuario.usuario or Usuario.email == usuario.email
            )
    )

    if db_user:
        if db_user.usuario == usuario.usuario:
            raise HTTPException(status_code = HTTPStatus.BAD_REQUEST, detail = 'Usuário já existe')
        if db_user.email == usuario.email:
            raise HTTPException(status_code = HTTPStatus.BAD_REQUEST, detail = 'Email já existe')
    
    db_user = Usuario(usuario=usuario.usuario, email=usuario.email, senha=usuario.senha)

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user

@app.get('/users/', response_model=UsuarioList)
def read_users():
    ...

@app.put('/users/{user_id}', response_model=UsuarioPublic)
def read_user(user_id: int, users: UsuarioSchema):
    ...


@app.delete('/users/{user_id}', response_model=Mensagem)
def delete_user(user_id: int):
    ...