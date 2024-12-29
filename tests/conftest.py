import requests
import pytest 
from configuration.config import LOGIN_USER

"""
under test folder we create a file coftest
pytest will look for the file to retrive this fixtures
We can real life scenerio the password will not be hardcoded
"""
@pytest.fixture(scope="session")
def login_user():
    payload = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"

    }
    response = requests.post(f'{LOGIN_USER}', data=payload)
    assert response.status_code == 200
    # If the login require authorization header token
    token = response.json()["token"]
    return token 

"""
login as invalid user
"""
@pytest.fixture(scope="session")
def invalid_user():
    payload = {
             "email": "peter@klaven"
            }

    response = requests.post(f'{LOGIN_USER}', data=payload)
    assert response.status_code == 400
    # There wont be any Authorization token because the user login failed
    token = response.json()
    return token