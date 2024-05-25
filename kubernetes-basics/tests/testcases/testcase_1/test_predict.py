from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_predict():
    response = client.post(
        "/v1/topic_model_predict",
        headers={
            "accept": "application/json", "Content-Type": "application/json"
            },
        json={
            "text": "car lock not working"
        },
    )

    assert response.status_code == 200
