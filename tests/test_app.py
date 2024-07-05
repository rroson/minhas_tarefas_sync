from http import HTTPStatus
from fastapi.testclient import TestClient
from minhas_tarefas.app import app

# Escrever testes com nomes descritivos
def test_read_root_deve_retornar_ok_e_olamundo():
    client = TestClient(app) # Arrange (Organização do teste)
    response = client.get('/') # Act (Ação do teste)
    assert response.status_code == HTTPStatus.OK # Assert (Validação do teste)
    assert response.json() == {'Message': 'Olá mundo!'}