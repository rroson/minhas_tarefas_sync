from http import HTTPStatus
from fastapi import FastAPI, HTTPException
from minhas_tarefas.schemas import Mensagem, UsuarioSchema, UsuarioPublic, UsuarioDB, UsuarioList


app = FastAPI()
database = [] #Fake Database

@app.get("/", status_code=HTTPStatus.OK, response_model=Mensagem)
def read_root():
    return {'mensagem': 'Olá mundo!'}

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

@app.put('/users/{user_id}', response_model=UsuarioPublic)
def read_user(user_id: int, users: UsuarioSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code = HTTPStatus.NOT_FOUND, detail = 'Usuário não encontrado')
    user_with_id = UsuarioDB(**users.model_dump(), id = user_id)
    database[user_id - 1] = user_with_id

    return user_with_id

@app.delete('/users/{user_id}', response_model=Mensagem)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code = HTTPStatus.NOT_FOUND, detail = 'Usuário não encontrado')
    del database[user_id - 1]
    return {'mensagem': 'Usuário excluído com sucesso'}