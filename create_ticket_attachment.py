## This script requires "requests": http://docs.python-requests.org/
## To install: pip install requests

import requests
import json

api_key = "DkvRUEwv1N6BlA8oD"
domain = "idealplanportal"
password = "aRLAEHDRJS1234"

headers = { 'Content-Type' : 'application/json' }

ticket = {
    'subject' : 'I have got a new plan, what should I do?',
    'description' : 'Test System Test',
    'email' : 'nkim@nexiacanberra.com.au',
    'type' : 'General enquiry',
    'priority' : 1,
    'status' : 2,
}

r = requests.post("https://"+ domain +".freshdesk.com/api/v2/tickets", auth = (api_key, password), headers = headers, data = json.dumps(ticket))

if r.status_code == 201:
  print ("Ticket created successfully, the response is given below")
  print (r.content)
  print ("Location Header : ")
  print (r.headers['Location'])
else:
  print ("Failed to create ticket, errors are displayed below,")
  response = json.loads(r.content)
  print (response["errors"])

  print ("x-request-id : ")
  print (r.headers['x-request-id'])
  print ("Status Code : ")
  print (str(r.status_code))