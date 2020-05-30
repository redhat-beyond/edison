def test_app_running(client):
    assert client.get('/').status_code == 200
