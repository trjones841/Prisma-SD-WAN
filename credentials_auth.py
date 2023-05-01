'''
Login using credentials

'''

import requests
import json
import secrets

url = "https://api.elcapitan.cloudgenix.com/v2.0/api/login"
#url = "https://api.hood.cloudgenix.com/v2.0/api/login"
#url = 'https://login.hood.cloudgenix.com/sign-in.html?username=tjones@war-eagle.me&submit=true'

payload = json.dumps({
  "email": secrets.email,
  "password": secrets.passwd
})
headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_1) AppleWebKit/534.48.3 (KHTML, like Gecko) Version/5.1 Safari/534.48.3',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
if response.status_code == 200:
  print('creds_auth:\n', json.dumps(response.json(), indent=4))
elif response.status_code == 403:
  print('creds_auth: Request Failed with authorization failure: ' + str(response.status_code))
else:
  print('creds_auth: Request Failed with status code: ' + str(response.status_code))
  print('creds_auth: Request URL: ', url)
