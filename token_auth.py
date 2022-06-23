'''
Login using authentication token, then run the API call

'''
__author__ = 'Terry Jones'
__date__ = '20JUN2022'
__version__ = '0.1'

#***********************************************************************************************************************
# Import Libraries
#***********************************************************************************************************************
import requests
import json
import secrets

#***********************************************************************************************************************
# Variables
#***********************************************************************************************************************
url = "https://api.hood.cloudgenix.com"
token = secrets.hood_auth_token4

site_id = '16401369439180122' # Terry's Lab
#site_id = '16407461458420099' #Branch02
#site_id = '16413196971540035' #Branch01
#site_id = '16411652632420028' #Azure-SouthCentral-DC
#site_id = '16412530301000165' #US Central

element_id = '16400363208000224'
interface_id = '16400366754900050'
null = None
headers = {
  'x-auth-token': token,
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_1) AppleWebKit/534.48.3 (KHTML, like Gecko) Version/5.1 Safari/534.48.3',
  'Content-Type': 'application/json'
}
interface_id = secrets.interface_id
tenantID = secrets.tenantID
false = False
true = True
#***********************************************************************************************************************
# Run these commands only if this file is called directly
#***********************************************************************************************************************
if __name__ == "__main__":

  run_all = 0
  get_profile = 0
  get_sites = 0
  get_elements = 0
  get_topApps = 0
  get_health = 0
  get_bgp_peer = 0
  update_bgp_peer = 0
  get_monitor_flows = 0
  get_interfaces = 0
  get_interface_N = 1
  get_interface_status = 0
  set_interface_down = 0

  # Get Profile
  profile_api = '/v2.0/api/profile'
  if run_all | get_profile:
    response = requests.request("GET", url+profile_api, headers=headers)
    if response.status_code == 200:
      print('profile_api\n', json.dumps(response.json(), indent=4))
    elif response.status_code == 403:
      print('profile_api: Request Failed with authorization failire: ' + str(response.status_code))
    else:
      print('profile_api: Request Failed with status code: ' + str(response.status_code))
      print('profile_api: Request URL: ' + profile_api)
  else:
    print('Skipped Get Profile')


  # Get Sites
  sites_api = '/v4.5/api/tenants/' + tenantID + '/sites'
  if run_all | get_sites:
    response = requests.request("GET", url + sites_api, headers=headers)
    if response.status_code == 200:
      print('sites_api:\n',json.dumps(response.json(), indent=4))
    elif response.status_code == 403:
      print('sites_api: Request Failed with authorization failire: ' + str(response.status_code))
    else:
      print('sites_api: Request Failed with status code: '+ str(response.status_code))
      print('sites_api: Request URL: '+sites_api)
  else:
    print("Skipped Get Sites")


    # Get Elements for all sites
    elements_api = '/v2.4/api/tenants/' + tenantID + '/elements'
    if run_all | get_elements:
      response = requests.request("GET", url + elements_api, headers=headers)
      if response.status_code == 200:
        print('elements_api:\n', json.dumps(response.json(), indent=4))
      elif response.status_code == 403:
        print('elements_api: Request Failed with authorization failire: ' + str(response.status_code))
      else:
        print('elements_api: Request Failed with status code: ' + str(response.status_code))
        print('elements_api: Request URL: ' + elements_api)
    else:
      print("Skipped Get Elements")


  #Print the Top Applications for the given site
  topApps_api = '/v3.0/api/tenants/' + tenantID + '/monitor/topn'
  if run_all | get_topApps :
    payload = json.dumps({
      "topn_basis": "traffic_volume",
      "top_n": {
        "type": "app",
        "limit": 10
      },
      "filter": {
        "site": [
          "16401369439180122"
        ]
      },
      "start_time": "2022-06-18T09:00:00.380Z",
      "end_time": "2022-06-18T17:00:00.380Z"
    })
    response = requests.request("POST", url + topApps_api, headers=headers, data=payload)
    if response.status_code == 200:
      print('topApps_api:\n',json.dumps(response.json(), indent=4))
    elif response.status_code == 403:
      'Request Failed with authorization failire: ' + str(response.status_code)
    else:
      print('TopApps: Request Failed with status code: ' + str(response.status_code))
      print('Reques URL: ' + topApps_api)
  else:
    print("Skipped Get TopApps")


  # Get BGP peer for site  (16401369439180122 - Terry's Lab)
  bgp_peer_api ='/v2.2/api/tenants/' + tenantID + '/sites/' + site_id + '/elements/16400363208000224/bgppeers/16446944105550117'
  if run_all | get_bgp_peer :
    response = requests.request("GET", url + bgp_peer_api, headers=headers)
    if response.status_code == 200:
      print('bgp_peer_api:\n', json.dumps(response.json(), indent=4))
    elif response.status_code == 403:
      print('bgp_peer_api: Request Failed with authorization failire: ' + str(response.status_code))
    else:
      print('bgp_peer_api: Request Failed with status code: ' + str(response.status_code))
      print('bgp_peer_api: Request URL: ' + bgp_peer_api)
  else:
    print("Skipped Get BGP Peers")

  # Update the bgp peering settings for the PRISMA_ONPREM_DR peer
  '''payload = json.dumps({
    "id": "16401949221120075",
    "_etag": 4,
    "_content_length": "0",
    "_schema": 1,
    "_created_on_utc": 16401949221120075,
    "_updated_on_utc": 16402993982690193,
    "_status_code": "200",
    "_request_id": "1655752583211017300003197556962864429983",
    "_debug": null,
    "_info": null,
    "_warning": null,
    "_error": null,
    "name": "PA-VM-DR",
    "description": "LAN side BGP peer - updated again",
    "tags": null,
    "peer_ip": "172.16.1.1",
    "remote_as_num": "65102",
    "peer_type": "classic",
    "route_map_in_id": null,
    "route_map_out_id": null,
    "update_source": null,
    "bgp_config": null,
    "shutdown": false,
    "scope": "global"
  })'''
  payload = json.dumps({
    "id": "16446944105550117",
    "_etag": 11,
    "_content_length": "0",
    "_schema": 1,
    "_created_on_utc": 16446944105550117,
    "_updated_on_utc": 16557509481620118,
    "_status_code": "200",
    "_request_id": "1655780954152004400003326036603348177934",
    "_debug": null,
    "_info": null,
    "_warning": null,
    "_error": null,
    "name": "PRISMA_ONPREM_DR",
    "description": "BGP peering for Prisma Access for DR site (Panorama)",
    "tags": null,
    "peer_ip": "192.168.155.9",
    "remote_as_num": "65155",
    "peer_type": "classic",
    "route_map_in_id": null,
    "route_map_out_id": null,
    "update_source": "10.100.100.9",
    "bgp_config": null,
    "shutdown": false,
    "scope": "global"
  })
  #peer = '16401949221120075'
  peer = '16446944105550117'
  update_bgppeers_api = '/v2.2/api/tenants/' + tenantID + '/sites/' + site_id + '/elements/16400363208000224/bgppeers/' + peer
  if run_all | update_bgp_peer :
    response = requests.request("PUT", url + update_bgppeers_api, headers=headers, data=payload)
    if response.status_code == 200:
      print('update_bgppeers_api:\n', json.dumps(response.json(), indent=4))
    elif response.status_code == 403:
      print('update_bgppeers_api: Request Failed with authorization failure: ' + str(response.status_code))
    else:
      print('update_bgppeers_api: Request Failed with status code: ' + str(response.status_code))
      print('update_bgppeers_api: Request URL: ' + update_bgppeers_api)
  else:
    print("Skipped Update BGP Peers")

  #Get Monitor Flows - POST /v3.6/api/tenants/[tenant_id]/monitor/flows
  payload = json.dumps({
    "start_time": "2022-06-13T17:22:22.609Z",
    "end_time": "2022-06-18T18:22:22.609Z",
    "filter": {
      "site": [ "[16401369439180122]" ]
    },
    "debug_level": "all"
  })
  monitor_flows_api = '/v4.10/api/tenants/' + tenantID + '/sites/16401369439180122/elements/16400363208000224/interfaces'
  if run_all | get_monitor_flows :
    response = requests.request("GET", url + monitor_flows_api, headers=headers)
    if response.status_code == 200:
      print('monitor_flows_api:\n', json.dumps(response.json(), indent=4))
    elif response.status_code == 403:
      print('monitor_flows_api: Request Failed with authorization failure: ' + str(response.status_code))
    else:
      print('monitor_flows_api: Request Failed with status code: ' + str(response.status_code))
      print('monitor_flows_api: Request URL: ' + monitor_flows_api)
  else:
    print("Skipped Monitor Flows")


  #Get Interfaces
  interfaces_api = '/v4.10/api/tenants/' + tenantID + '/sites/16401369439180122/elements/16400363208000224/interfaces'
  if run_all | get_interfaces :
    response = requests.request("GET", url + interfaces_api, headers=headers)
    if response.status_code == 200:
      print('interfaces_api:\n', json.dumps(response.json(), indent=4))
    elif response.status_code == 403:
      print('interfaces_api: Request Failed with authorization failure: ' + str(response.status_code))
    else:
      print('interfaces_api: Request Failed with status code: ' + str(response.status_code))
      print('interfaces_api: Request URL: ' + interfaces_api)
  else:
    print("Skipped Get Interfaces")


  #Get Specific Interface
  interfaceN_api = '/v4.10/api/tenants/' + tenantID + '/sites/16401369439180122/elements/16400363208000224/interfaces/16400366754900050'
  if run_all | get_interface_N :
    response = requests.request("GET", url + interfaceN_api, headers=headers)
    if response.status_code == 200:
      print('interfaceN_api:\n', json.dumps(response.json(), indent=4))
    elif response.status_code == 403:
      print('interfaceN_api: Request Failed with authorization failure: ' + str(response.status_code))
    else:
      print('interfaceN_api: Request Failed with status code: ' + str(response.status_code))
      print('interfaceN_api: Request URL: ' + interfaceN_api)
  else:
    print("Skipped Get Interface N")


  #Get Interface Status
  interfaces_status_api = '/v3.2/api/tenants/' + tenantID + '/sites/16401369439180122/elements/16400363208000224/interfaces/16400366754900050/status'
  if run_all | get_interface_status :
    response = requests.request("GET", url + interfaces_status_api, headers=headers)
    if response.status_code == 200:
      print('interfaces_status_api:\n', json.dumps(response.json(), indent=4))
    elif response.status_code == 403:
      print('interfaces_status_api: Request Failed with authorization failure: ' + str(response.status_code))
    else:
      print('interfaces_status_api: Request Failed with status code: ' + str(response.status_code))
      print('interfaces_status_api: Request URL: ' + interfaces_status_api)
  else:
    print("Skipped Get Interface N")


  #Set Interface Down
  payload = json.dumps({
    "id": "16400366754900050",
    "_etag": 20,
    "_schema": 4,
    "type": "port",
    "attached_lan_networks": null,
    "site_wan_interface_ids": [
        "16401369444750159"
    ],
    "name": "3",
    "description": "Cox Residential - Updated",
    "tags": null,
    "mac_address": null,
    "mtu": 1500,
    "ipv4_config": {
        "type": "dhcp",
        "static_config": null,
        "dhcp_config": null,
        "dns_v4_config": null,
        "routes": null
    },
    "ipv6_config": null,
    "ethernet_port": {
        "full_duplex": false,
        "speed": 0
    },
    "admin_up": true,
    "nat_address": null,
    "nat_port": 0,
    "nat_address_v6": null,
    "nat_port_v6": 0,
    "nat_zone_id": "16334700181070045",
    "nat_pools": null,
    "used_for": "public",
    "bypass_pair": null,
    "bound_interfaces": null,
    "sub_interface": null,
    "pppoe_config": null,
    "secondary_ip_configs": null,
    "static_arp_configs": null,
    "dhcp_relay": null,
    "parent": null,
    "network_context_id": null,
    "ipfixcollectorcontext_id": null,
    "ipfixfiltercontext_id": null,
    "service_link_config": null,
    "cellular_config": null,
    "multicast_config": {
        "multicast_enabled": false,
        "igmp_version": "IGMPV3",
        "dr_priority": null,
        "igmp_static_joins": null
    },
    "scope": "global",
    "devicemgmt_policysetstack_id": null,
    "directed_broadcast": false
  })
  interface_down_api = '/v4.12/api/tenants/' + tenantID + '/sites/' + site_id + '/elements/' + element_id + '/interfaces/'+ interface_id
  if run_all | set_interface_down:
    response = requests.request("PUT", url + interface_down_api, headers=headers, data=payload)
    if response.status_code == 200:
      print('interface_down_api: ', json.dumps(response.json(), indent=4))
    else:
      print('interface_down_api: Request failed with the status code: ' + str(response.status_code))
      print('interface_down_api: url: ' + interface_down_api)
  else:
    print('Skipped Set Interface Down.')


  # Get Health
  if run_all == 1 | get_health == 1:
    site_id = str(16401369439180122)
    payload = json.dumps({"type": "basenet","nodes": [site_id]})
    health_api = '/v3.3/api/tenants/'+ tenantID +'/topology'
    response = requests.request("POST", url + health_api, headers=headers, data=payload)
    if response.status_code == 200:
      print('health_api: \n',json.dumps(response.json(), indent=4))
    else:
      print('health_api: Request failed with the status code: ' + str(response.status_code))
  else:
    print('Skipped Get Health')
