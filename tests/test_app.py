from http import HTTPStatus

# Escrever testes com nomes descritivos
def test_read_root_deve_retornar_ok_e_olamundo(client):
    # client = TestClient(app) # Arrange (Organização do teste) #Substituido por client (fixture)
    response = client.get('/') # Act (Ação do teste)
    assert response.status_code == HTTPStatus.OK # Assert (Validação do teste)
    assert response.json() == {'mensagem': 'Olá mundo!'}

def test_create_user(client):
    # client = TestClient(app) # Substituido por client (fixture)
    response = client.post( # User Schema (Modelo de Usuário)
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    # Voltou o status code correto?
    assert response.status_code == HTTPStatus.CREATED
    # Validar UserPublic (Modelo de Usuário Publico)
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }

def test_read_users(client):
    respones = client.get('/users/')
    assert respones.status_code == HTTPStatus.OK
    assert respones.json() == {
        'users': [
            {
                'username': 'alice',
                'email': 'alice@example.com',
                'id': 1,
            }
        ]
    }

def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }

def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'mensagem': 'Usuário excluído com sucesso'}