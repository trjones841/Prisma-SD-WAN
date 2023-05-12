'''
Prisma SD-WAN - Unified API

This script will call the sdwan_auth.py script first to authenticate and return a bearer token.

https://pan.dev/sase/docs/api-call/

curl -o --location "https://api.sase.paloaltonetworks.com/config/v1/jobs" \
-H "Authorization: Bearer <ACCESS_TOKEN>" \
-H "Content-Type: application/json"

'''
author = 'Terry Jones'
__author__ = '%s' % author
__date__ = '29APR2023'
__version__ = '0.1'

import requests
import json
import sdwan_auth
from secrets import jeg_auth_token
# from secrets import jeg_tenant_id as tenant_id


def set_profile(token):
    path = '/sdwan/v2.1/api/profile'
    headers = {
        'Authorization': 'Bearer ' + str(token),
        'Content-Type': 'application/json',
    }
    url = 'https://api.sase.paloaltonetworks.com' + path
    return requests.get(url, headers=headers)


def get_jobs(token):
    path = '/config/v1/jobs'
    headers = {
        'Authorization': 'Bearer ' + str(token),
        'Content-Type': 'application/json',
    }
    url = 'https://api.sase.paloaltonetworks.com' + path
    return requests.get(url, headers=headers)


def get_sites(token):
    path = '/sdwan/v4.7/api/sites'
    headers = {
        'Authorization': 'Bearer ' + str(token),
        'Content-Type': 'application/json',
    }
    payload = {}
    url = 'https://api.sase.paloaltonetworks.com' + path
    response = requests.get(url, headers=headers, data=payload)
    return response.json()


def site_ids (sitesinfo):  #takes input from site call to return site id w/ associated site name
    site_info = {key: sitesinfo['items'] for key in sitesinfo.keys() & {'items'}}
    data = site_info['items']
    result = {}
    print(json.dumps(sitesinfo,indent=4))
    for item in data:
        result[item['id']] = item['name']

    return result


def get_site_data(site_id, token):
    path = '/sdwan/v4.7/api/sites/' + site_id
    headers = {
        'Authorization': 'Bearer ' + str(token),
        'Content-Type': 'application/json',
    }
    payload = {}
    url = 'https://api.sase.paloaltonetworks.com' + path
    response = requests.get(url, headers=headers, data=payload)
    return response.json()

def get_site_lannetworks(site_id, token):
    path = '/sdwan/v3.1/api/sites/' + site_id + '/lannetworks'
    headers = {
        'Authorization': 'Bearer ' + str(token),
        'Content-Type': 'application/json',
    }
    payload = {}
    url = 'https://api.sase.paloaltonetworks.com' + path
    response = requests.get(url, headers=headers, data=payload)
    return response.json()

# GET /sdwan/v2.1/api/sites/:site_id/waninterfaces
# POST /v2.0/api/tenants/1112129370/logout
# GET /sdwan/v4.4/api/sites/:site_id


if __name__ == '__main__':
    bearer_token = sdwan_auth.bearer_token()
    # set_profile required for all API once the bearer token request is made.
    print('tenant_id: ', json.dumps(set_profile(bearer_token).json()['tenant_id'], indent=4))

    get_site_ids = 1
    if get_site_ids == 1:
        sites = get_sites(bearer_token)  # API call to get all info for all sites configured.
        list_sites_id = site_ids(sites)  # Extracts the site id w/ associated site name
        print(json.dumps(list_sites_id, indent=4))

    get_site_info = 0
    siteID = '1682708421285002296'
    if get_site_info == 1:
        result = get_site_data(siteID, bearer_token)
        print(json.dumps(result, indent=4))

    lannetworks = 0
    if lannetworks == 1:
        result = get_site_lannetworks(siteID, bearer_token)
        print(json.dumps(result, indent=4))
