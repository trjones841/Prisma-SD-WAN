'''


'''
author = 'Terry Jones'
__author__ = '%s' % author
__date__ = '29APR2023'
__version__ = '0.1'

import requests
import json
import sdwan_auth
from secrets import auth_token
from site_info_payload import site_level_data
from site_info_payload import lannetworks_data


def set_profile(token):
    path = '/sdwan/v2.1/api/profile'
    headers = {
        'Authorization': 'Bearer ' + str(token),
        'Content-Type': 'application/json',
    }
    url = 'https://api.sase.paloaltonetworks.com' + path
    return requests.get(url, headers=headers)


def post_site_lannetworks(data, site_id, token):
    path = '/sdwan/v3.2/api/sites/' + site_id + '/lannetworks'
    headers = {
        'Authorization': 'Bearer ' + str(token),
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    url = 'https://api.sase.paloaltonetworks.com' + path
    response = requests.post(url, headers=headers, data=data)
    return response


if __name__ == '__main__':
    null = None
    siteID = '1682708421285002296'
    bearer_token = sdwan_auth.bearer_token()
    print('tenant_id: ', json.dumps(set_profile(bearer_token).json()['tenant_id'], indent=4))
    print(post_site_lannetworks(lannetworks_data, siteID, bearer_token))

