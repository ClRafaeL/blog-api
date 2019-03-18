import json

def test_home_response_hello(client):
    """
    **Given** Luiza está acessando a API,
    **When** ela informa a rota/endpoint `/`,
    **Then** a api deve responder um objeto com a chave `['hello']`,
    **And** seu conteúdo deve ser `world by apps`
    """
    
    response = client.get('/')

    data = json.loads(response.data.decode('utf-8'))

    assert data['hello'] == 'world by apps'