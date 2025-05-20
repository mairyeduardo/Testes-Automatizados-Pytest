from test.utils.e2e_payloads.payload_user import *
from test.utils.requestToTest.request_to_test import request_to_test


class TestUser:
    URL = "https://api-qas-trainings.glitch.me/users"
    request_to_specific_url = f"{URL}/3"

    def test_create_user(self, url=URL):
        response = request_to_test("POST", url, PAYLOAD_TO_CREATE_USER)
        data = response.json()
        assert response.status_code == 201
        assert data["name"] == PAYLOAD_TO_CREATE_USER["name"]
        assert data["email"] == PAYLOAD_TO_CREATE_USER["email"]

    def test_get_user_by_id(self, url=request_to_specific_url):
        response = request_to_test("GET", url)
        data = response.json()
        assert response.status_code == 200
        assert data["id"] == 3
        assert data["name"] == PAYLOAD_TO_CREATE_USER["name"]
        assert data["email"] == PAYLOAD_TO_CREATE_USER["email"]

