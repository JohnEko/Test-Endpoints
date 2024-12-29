import requests 
import pytest
import json
from src.utilities.headerUtilities import url_header 
from configuration.config import LOG


class SasUtilities:

    def __init__(self):
        self.sas = "/api/users"


    def get_all_users(self, base_url, token):
        header = url_header(token)
        response = requests.get(f"{base_url}{self.sas}", headers=header, verify=False)
        return response 
    
    
    def get_specific_user(self, base_url, token, user):
        header = url_header(token)
        response = requests.get(f"{base_url}{self.sas}/{user}", headers=header)
        return response 
    
    def get_invalid_user_id(self, base_url, token, user):
        header = url_header(token)
        response = requests.get(f"{base_url}{self.sas}/{user}", headers=header)
        return response 
    
    def create(self, base_url, token):
        header = url_header(token)
        payload ={"name": "SAS Technical Task",
                   "job": "Test Automation"
                 }
        LOG.debug(f"Newly created user: {payload}" )      
        response = requests.post(f"{base_url}{self.sas}/", headers=header, data=payload)
        return response
    

    def delete_user(self, base_url, token, user):
        header = url_header(token)
        response = requests.delete(f"{base_url}{self.sas}/{user}", headers=header)
        return response 

