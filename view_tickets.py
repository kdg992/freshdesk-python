## This script requires "requests": http://docs.python-requests.org/
## To install: pip install requests

import requests
import json

api_key = "DkvRUEwv1N6BlA8oD"
domain = "idealplanportal"
password = "aRLAEHDRJS1234"

# Id of the ticket to be updated
ticket_id = '67780'

r = requests.get("https://"+ domain +".freshdesk.com/api/v2/tickets/"+ticket_id, auth = (api_key, password))

if r.status_code == 200:
  print ("Successful")
  print (r.content)
else:
  print ("Failed to read ticket, errors are displayed below,")
  response = json.loads(r.content)
  print (response["errors"])

  print ("x-request-id : " + r.headers['x-request-id'])
  print ("Status Code : " + r.status_code)