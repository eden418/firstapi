import requests

BASE = "http://127.0.0.1:5000/"

# The put method in a request allows us to send some information not via the address.
# The data we send is received in a form
response = requests.put(BASE + "video/1", {"likes": 10})
print(response.json())
