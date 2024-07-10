import pytest
from fastapi.testclient import TestClient

from minhas_tarefas.app import app


@pytest.fixture()
def client():
    return TestClient(app)