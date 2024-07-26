from sqlalchemy import select
from minhas_tarefas.models import Usuario

def test_criar_usuario(session):
    usuario = Usuario(
        usuario='test_user',
        email='V9j2z@example.com',
        senha='test1234'
    )
    session.add(usuario)
    session.commit()
    # session.refresh(usuario) # Atualiza o objeto com os dados do banco
    result = session.scalar(
       select(Usuario).where(Usuario.email == 'V9j2z@example.com')
    )

    # assert result.usuario == 'test_user'
    assert result.id == 1