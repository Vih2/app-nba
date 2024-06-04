import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_resultados_nba(client):
    response = client.get('/v1/resultados_nba')
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 3
    assert data[0]['time_casa'] == "Los Angeles Lakers"
    assert data[1]['time_visitante'] == "Milwaukee Bucks"
    assert data[2]['pontos_visitante'] == 102
