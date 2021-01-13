import requests

url = "https://sandboxdnac.cisco.com:443/api/system/v1/auth/token"

payload={}
headers = {
  '': '',
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
