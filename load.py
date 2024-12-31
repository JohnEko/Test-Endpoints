from concurrent.futures import ThreadPoolExecutor
import json
import random
import time
import requests
from src.utilities.headerUtilities import url_header

number_of_requests = 100
base_url = ["https://reqres.in/api/users"]

paload = {"name": "SAS Technical Task",
          "job": "Test Automation"
         }

with open('payload') as f:
    PAYLOAD = json.load(f)

def send_post_request(url, data):
    header = url_header()
    response=requests.post(url, params=json.dumps(data), headers=header)
    return response.status_code

def main():

    record = [{**PAYLOAD} for _ in range(number_of_requests)]
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(send_post_request, base_url*number_of_requests, record)

        status_code_count = {}
        count = 0
        for result in results:
            if count % 10 == 0:
                print(status_code_count)
            status_code_count[result] = status_code_count.get(result, 0) + 1
            count += 1
        print(status_code_count)

if __name__=='__main__':
    main()