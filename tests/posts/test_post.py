def test_find_all(client):
    response = client.get('/posts/')

    assert response.status_code == 200

def test_find_bad_id(client):
    response = client.get('/posts/1')

    assert response.status_code == 400

def test_find_not_found(client):
    response = client.get('/posts/5c982631e7798941208914a1')

    assert response.status_code == 404

def test_delete_not_found(client):
    response = client.delete('/posts/5c982631e7798941208914a1')

    assert response.status_code == 404

def test_post_bad_request(client):
    response = client.post('/posts/')

    assert response.status_code == 400

def test_post_bad_request(client):
    response = client.post('/posts/')

    assert response.status_code == 400

def test_put_bad_resquest(client):
    response = client.put('/posts/5c982631e7798941208914a1')

    assert response.status_code == 400

