from pydantic import BaseModel, EmailStr


class Mensagem(BaseModel):
    mensagem: str

class UsuarioSchema(BaseModel):
    username: str
    email: EmailStr
    password: str

class UsuarioDB(UsuarioSchema):
    id: int

class UsuarioPublic(BaseModel):
    id: int
    username: str
    email: EmailStr

class UsuarioList(BaseModel):
    users: list[UsuarioPublic]