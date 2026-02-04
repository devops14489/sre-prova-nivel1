import sys
sys.path.insert(0, '../app')

from app import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """Testa se o endpoint principal funciona"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert 'message' in data
    assert 'version' in data

def test_health_endpoint(client):
    """Testa se o endpoint de saúde funciona"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_request_counter(client):
    """Testa se o contador de requisições funciona"""
    # faz uma chamada que incrementa total_requests
    client.get("/")

    m1 = client.get("/metrics").get_json()
    count1 = m1["total_requests"]

    client.get("/")

    m2 = client.get("/metrics").get_json()
    count2 = m2["total_requests"]

    assert count2 > count1

