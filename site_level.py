# ***********************************************************************************************************************
# Import Libraries
# ***********************************************************************************************************************
import requests
import json
import secrets

# ***********************************************************************************************************************
# Variables
# ***********************************************************************************************************************
url = secrets.url_hood
site_id = secrets.site_id
headers = secrets.headers
interface_id = secrets.interface_id
tenantID = secrets.tenantID
false = False
true = True
null = None
run_all = 0
get_specific_site = 1

if __name__ == '__main__':
    # Get Site US Central
    specific_site_api = '/v4.5/api/tenants/' + tenantID + '/sites/16412530301000165'
    if run_all | get_specific_site:
        response = requests.request("GET", url + specific_site_api, headers=headers)
        if response.status_code == 200:
            # print('specific_site_api:\n', json.dumps(response.json(), indent=4))
            print("\n")
        elif response.status_code == 403:
            print('specific_site_api: Request Failed with authorization failure: ' + str(response.status_code))
        else:
            print('specific_site_api: Request Failed with status code: ' + str(response.status_code))
            print('specific_site_api: Request URL: ' + sites_api)
    else:
        print("Skipped Get Specific Site")

    print('\n\nUpdating the dictionary\n\n')

    '''
    # One method to update the dictionary for a given object - using update method. 
    #Change_to_be_made = {"name": "US Central 1"}
    Change_to_be_made = {"address": {"street2": "Azure Datacenter"}}  # Replaced entire address dict with only street2
    updated_response = response.json()
    print('type: ', type(updated_response))
    updated_response.update(Change_to_be_made)
    print(json.dumps(updated_response, indent=4))
    '''

    key = 'address'
    obj = response.json()
    print(type(obj))
    if key in obj.keys():
        print('Key exist, ', end=' ')
        obj['address']['street2'] = 'its another street'
        obj['location']['description'] = 'IOWA'
        #obj['admin_state'] = 'disabled'
        print(json.dumps(obj, indent=4))
    else:
        raise Exception('Does not exist!')
