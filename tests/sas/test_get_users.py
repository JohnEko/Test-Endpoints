import pytest
from src.utilities.sasUtilities import SasUtilities
from configuration.config import BASE_URL, LOG



def test_valid_login_user(login_user):
    LOG.info("Test login with a valid user credentials")
    response = login_user
    LOG.debug(response)
    assert response

def test_invalid_login_user(invalid_user):
    LOG.info("Test login invalid user credentials user API")
    response = invalid_user
    LOG.debug(response)
    assert response


def test_get_all_user(login_user):
    LOG.info("Test to get every user from the API")
    response = SasUtilities().get_all_users(BASE_URL, login_user)
    LOG.debug(response.json())
    print(response.json()["per_page"])
    assert response.status_code == 200 
    assert response.json()['per_page'] == 6

def test_specific_user(login_user):
    """Test for valid user id and validate API response"""
    LOG.info("Test get a single user exist in the API")
    response = SasUtilities().get_specific_user(BASE_URL, login_user, user=1)
    # import pdb;pdb.set_trace()
    response_json = response.json()
    print(response_json)
    LOG.debug(response_json)
    assert response_json == response.json()
    assert response.status_code == 200 


def test_invalid_user(login_user):
    """Test for invalid user id and validate API response"""
    LOG.info("Test a single user exist in the API")
    response = SasUtilities().get_invalid_user_id(BASE_URL, login_user, user=11020303)
    # import pdb;pdb.set_trace()
    response_json = response.json()
    print(response_json)
    LOG.debug(response_json)
    assert response_json == response.json()
    assert response.status_code == 404


def test_create_new_user(login_user):

    LOG.info("Create new user")
    response = SasUtilities().create(BASE_URL, login_user)
    assert response.ok
    response_json = response.json()
    assert response_json == response.json()
    assert response.status_code == 201
                 

def test_delete_user(login_user):
    LOG.info("Test to get every user from the API")
    response = SasUtilities().delete_user(BASE_URL, login_user, user=3)
    assert response.ok
    LOG.debug(response)
    assert response.status_code == 204