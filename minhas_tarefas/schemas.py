from pydantic import BaseModel, EmailStr


class Mensagem(BaseModel):
    mensagem: str

class UsuarioSchema(BaseModel):
    usuario: str
    email: EmailStr
    senha: str

class UsuarioDB(UsuarioSchema):
    id: int

class UsuarioPublic(BaseModel):
    id: int
    usuario: str
    email: EmailStr

class UsuarioList(BaseModel):
    users: list[UsuarioPublic]