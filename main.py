# Import the CloudGenix SDK API constructor and JSON response pretty printer
from cloudgenix import API, jd

# Instantiate the CloudGenix API constructor
sdk = API()
sdk.tenant_id = 2356
sdk.controller_region = 'hood'

# Call CloudGenix API login using the Interactive helpers (Handle SAML2.0 login and MSP functions too!).
sdk.interactive.login()
sdk.client_id = 4

# Print a dump of the list of sites for your selected account
# jd(sdk.get.sites())

interfaces = jd(sdk.get.interfaces_status)

print(interfaces)
