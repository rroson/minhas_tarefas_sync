import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from minhas_tarefas.app import app
from minhas_tarefas.models import tabela_registro


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture()
def session():
    engine = create_engine('sqlite:///:memory:', echo=True)
    tabela_registro.metadata.create_all(engine)
    with Session(engine) as session:
        yield session # Para de executar e retorna quando terminar o teste
    tabela_registro.metadata.drop_all(engine)