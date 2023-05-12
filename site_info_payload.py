import json

null = None

site_level_data = json.dumps({
    "_etag": 3,
    "_schema": 2,
    "id": "1682708421285002296",
    "name": "CH2M-USGNV2 (Gainsville, FL)",
    "description": "CH2M-USGNV2 (Gainsville, FL)\nSite Contact:\nMike Thomas\nMike.Thomas@jacobs.com\n352-284-5892",
    "tags": null,
    "element_cluster_role": "SPOKE",
    "admin_state": "disabled",
    "address": {
        "street": "643 SW 4th Ave",
        "street2": "Suite 400",
        "city": "Gainsville",
        "state": "FL",
        "post_code": "32601",
        "country": "United States"
    },
    "location": {
        "longitude": -82.3309,
        "latitude": 29.64833,
        "description": null
    },
        "policy_set_id": null,
        "security_policyset_id": null,
        "network_policysetstack_id": "1682001805339021796",
        "priority_policysetstack_id": "1682001808670022996",
        "security_policysetstack_id": null,
        "nat_policysetstack_id": "1682001812919022896",
        "service_binding": "1682001814683022396",
        "extended_tags": null,
        "multicast_peer_group_id": null
    })


lannetworks_data = json.dumps({
    "name": "default_CH2M-USGNV2 (Gainsville,_476337304",
    "description": null,
    "tags": null,
    "ipv4_config": {
        "prefixes": [
            "102.238.0.0/24"
        ],
        "dhcp_relay": null,
        "dhcp_server": null,
        "default_routers": null
    },
    "ipv6_config": null,
    "scope": "global",
    "network_context_id": null
}
)
