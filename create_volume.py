vserver-get import requests
import json

url = "https://cluster1.demo.netapp.com/api/storage/volumes?return_timeout=0&return_records=false"

payload = json.dumps({
  "aggregates": [
    {
      "name": "cluster1_01_SSD_1"
    }
  ],
  "name": "{{vol_name}}",
  "size": "200mb",
  "svm": {
    "name": "svm1_cluster1"
  }
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic YWRtaW46TmV0YXBwMSE='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
