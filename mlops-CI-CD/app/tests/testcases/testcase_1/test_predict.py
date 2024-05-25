from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_predict(test_body, test_response):
    response = client.post(
        "/predict",
        headers={
            "accept": "application/json", "Content-Type": "application/json"
            },
        json=test_body,
    )

    assert response.status_code == 200
    print(response)
    print(test_response)
    # assert response.body == test_response
