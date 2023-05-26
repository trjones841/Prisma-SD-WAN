'''
Prisma SD-WAN - Unified API

This script will call secret variables from secrets.py to generate an access token that will be
returned by this script to the caller.

returns <string type>

Reference: https://pan.dev/sase/docs/access-tokens/

curl --data "grant_type=client_credentials&scope=tsg_id:<tsg_id>" \
--user '<client_id>:<client_secret>' \
--header "Content-Type: application/x-www-form-urlencoded" \
-X POST https://auth.apps.paloaltonetworks.com/oauth2/access_token

'''
author = 'Terry Jones'
__author__ = '%s' % author
__date__ = '29APR2023'
__version__ = '0.1'

import requests
from secrets import jeg_tenant_id as tenant_id
from secrets import auth_endpoint as url
from secrets import svc_acct
from secrets import client_secret


def bearer_token():
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = 'grant_type=client_credentials&scope=tsg_id:' + tenant_id

    #Need to add Try/Except here to handle failures
    response = requests.post(url, headers=headers, data=data, auth=(svc_acct, client_secret))
    return response.json()['access_token']


if __name__ == '__main__':
    print(bearer_token())
