import json

def test_index_response_200(client):
    response = client.get('/')

    assert response.status_code == 200