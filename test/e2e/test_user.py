from test.utils.e2e_payloads.payload_user import *
from test.utils.requestToTest.request_to_test import request_to_test

class TestUser:
    URL = "https://api-qas-trainings.glitch.me/users"

    def test_create_user(self, url=URL):
        response = request_to_test("POST", url, PAYLOAD_TO_CREATE_USER)
        assert response.status_code == 201