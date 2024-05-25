from fastapi.testclient import TestClient
from main import app
import os

# fname = os.path.join(os.path.dirname(__file__), 'brain_events1.csv')
# client = TestClient(app)


# def test_build_model():
#     response = client.post(
#         "/v1/build_topic_model",
#         files=[('data', ('brain_events1.csv',
#                 open(fname, 'rb'), 'text/csv'))])

#     assert response.status_code == 200

client = TestClient(app)


def test_basic_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"About": "Khoros actiongen API"}
