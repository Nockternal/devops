import requests
from extras.scripts import *

url = "http://192.168.127.162:30080/api/v2/job_templates/11/launch/"

payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer fSISbYdZUNZ2N2QMPHO5Ahq2YjP4bt',
  'Cookie': 'csrftoken=tkHyX0vNLGCTIrXbCoWwq1AgOZj4VZEC'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)



class Test(Script):
    class Meta:
        name = "Test"
        description = "Test script"
        commit_default = False

    def run(self, data, commit):
        print("Test script")
        url = "http://192.168.127.162:30080/api/v2/job_templates/11/launch/"

        payload = {}
        headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer fSISbYdZUNZ2N2QMPHO5Ahq2YjP4bt',
        'Cookie': 'csrftoken=tkHyX0vNLGCTIrXbCoWwq1AgOZj4VZEC'
        }
        response = requests.request("POST", url, headers=headers, data=payload)


        return response.text