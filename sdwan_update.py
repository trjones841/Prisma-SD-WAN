'''


'''
author = 'Terry Jones'
__author__ = '%s' % author
__date__ = '29APR2023'
__version__ = '0.1'

import requests
import json
import sdwan_auth
from secrets import jeg_auth_token
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


def put_site_data(site_id, site_data, token):
    path = '/sdwan/v4.7/api/sites/' + site_id
    headers = {
        'Authorization': 'Bearer ' + str(token),
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    url = 'https://api.sase.paloaltonetworks.com' + path
    response = requests.put(url, headers=headers, data=site_data)
    return response.json()


def put_site_lannetworks(site_id, lannetwork_id, lan_data, token):
    path = '/sdwan/v3.1/api/sites/' + site_id + '/lannetworks/' + lannetwork_id
    headers = {
        'Authorization': 'Bearer ' + str(token),
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    url = 'https://api.sase.paloaltonetworks.com' + path
    print(lan_data)
    response = requests.put(url, headers=headers, data=lan_data)
    return response


if __name__ == '__main__':
    null = None
    bearer_token = sdwan_auth.bearer_token()
    print('tenant_id: ', json.dumps(set_profile(bearer_token).json()['tenant_id'], indent=4))

    site = '1682708421285002296'

    # Example using data from CH2M-USGNV2 (Gainsville, FL)
    siteleveldata = 0
    if siteleveldata == 1:
        print(put_site_data(site, site_level_data, bearer_token))

    sitelannetworks = 1
    if sitelannetworks == 1:
        lannetwork_id = '1682708421285002296'
        print(put_site_lannetworks(site, lannetwork_id, lannetworks_data, bearer_token))
