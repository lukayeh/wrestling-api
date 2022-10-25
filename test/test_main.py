import json

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

with open("app/pkg_info.json") as fp:
    info = json.load(fp)

__version__ = info["version"]


def test_get_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Wrestler API in Python",
        "version": __version__,
    }


# def test_get_wrestler_bad_id():
#     response = client.get("/wrestler?id=foo")
#     assert response.status_code == 422
#     assert response.json() == {
#         "detail": [
#             {
#                 "loc": ["query", "id"],
#                 "msg": "value is not a valid integer",
#                 "type": "type_error.integer",
#             }
#         ]
#     }

# def test_get_wrestler_good_id():
#     response = client.get("/wrestler?id=1")
#     assert response.status_code == 200
