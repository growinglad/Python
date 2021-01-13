import requests
import json


url = "https://sandboxdnac.cisco.com:443/dna/intent/api/v1/network-device"

payload={}
headers = {
  'x-auth-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI1ZTlkYmI3NzdjZDQ3ZTAwNGM2N2RkMGUiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVkYzQ0NGQ1MTQ4NWM1MDA0YzBmYjIxMiJdLCJ0ZW5hbnRJZCI6IjVkYzQ0NGQzMTQ4NWM1MDA0YzBmYjIwYiIsImV4cCI6MTYxMDU3OTEwNywiaWF0IjoxNjEwNTc1NTA3LCJqdGkiOiI4MzcxMDhhOS0zMTI3LTQxNzktYjNkNi1kNmIzZjY0ZmE2ZjMiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.I5KhYkzQBa7eLRILemWs3jKQK-hg5PUUMvHopYtjH4RBT7t5ZUff9X1HKL9_wKVV3Y2p7n9zpE7cmJQAUGIecrOiVP5RL4lJtDuwdziD0hfailpW202yjNNQawoZuTIYwtmXUvONCAqKiReqirIRc0vpHtEEsLG7x918QDNwW6y3ZEOY_zjNJC6vCKxR14-xDRaUjv7-YRgCAtNJhw8V0h6j9n_PWRPBIsOI0DMF2RqbF4prtgdKTWAEA9yUb_SW3NFOtW0SHpbJ9vMdUz3ULV5mbsALbGBVAq2AdUau_m30X2qNIKdggGPd4xgxJ9eKwmzc7Obaf5LTg8oISdN6sg'
}

response = requests.request("GET", url, headers=headers, data=payload)

raw_data = json.loads(response.text)

devices = raw_data["response"]

print(type(devices))

for device in devices:
    print("Hostname arroony: {}".format(device["hostname"]))
