'''

'''
__author__ = 'Terry Jones'
__version__ = '0.1'

import requests
import json
from secrets import api_endpoint
from secrets import headers
from secrets import interface_id
from secrets import element_id
from secrets import site_id
from secrets import tenant_id

# ***********************************************************************************************************************
# Variables
# ***********************************************************************************************************************


def update_call(api_object, change):
    try:
        response = requests.request("GET", api_endpoint + api_object, headers=headers)
        if response.status_code == 200:
            obj_response = response.json()
        elif response.status_code == 403:
            raise Exception('Request failed with authorization failure: ' + str(response.status_code))
        else:
            raise Exception('Check response code: ' + str(response.status_code))

        obj_response.update(change)

        return obj_response
    finally:
        print('Exception Occurred.')


if __name__ == '__main__':
    tenantID = tenant_id
    site_id = site_id
    api = '/v4.5/api/tenants/' + tenantID + '/sites/' + site_id
    Change_to_be_made = {"name": "US Central 2"}
    print(json.dumps(update_call(api, Change_to_be_made), indent=2))

