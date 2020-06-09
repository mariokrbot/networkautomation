import requests
import json
import csv
url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device/"

payload = {}
headers = {
  'X-Auth-Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI1ZWNmZDViMjc1MTYxMjAwY2M1NzI3ZGEiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlNWE0MzI2NzUxNjEyMDBjYzRhYzk2MyJdLCJ0ZW5hbnRJZCI6IjVlNWE0MzI1NzUxNjEyMDBjYzRhYzk1YyIsImV4cCI6MTU5MTM0NjA2NSwiaWF0IjoxNTkxMzQyNDY1LCJqdGkiOiJlZGQ5ODFiMS1iYTE4LTRlMzctOTVjMS02NzMxNGZiYzQ2YTMiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.GTClEEWvYJx0Bgusopl6_tqumgRmAfoxHJkR74GWj_ooN62lrx8UjZQltLPvShK7bPse1xHdqRvRop-rwocIKuE3tzqMvGOFFa2Rym76Gr-f7ofjEv1TKNc_YJjqtQBzrZU3R0niD4-dbLFjYS4gF4X7DCC4DuT5HQjI5g7H2VdFNNEjC2UAUq2Xtfyr47j-VcimiBuDf7GQ9jkW8W-ec9hHlB5kk0YOfS2enTU42S5pHziJIN-3T4vq26FPWP6g1CnFFjf9VoBJQrMsZyGNv-YqpO7A_aXbTGENh1YIeLHc7ObH-ztyhMRTurJoC-94b8J2wBGkDxzWma_PIMZngQ',
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI1ZWNmZDViMjc1MTYxMjAwY2M1NzI3ZGEiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlNWE0MzI2NzUxNjEyMDBjYzRhYzk2MyJdLCJ0ZW5hbnRJZCI6IjVlNWE0MzI1NzUxNjEyMDBjYzRhYzk1YyIsImV4cCI6MTU5MTM0NjA2NSwiaWF0IjoxNTkxMzQyNDY1LCJqdGkiOiJlZGQ5ODFiMS1iYTE4LTRlMzctOTVjMS02NzMxNGZiYzQ2YTMiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.GTClEEWvYJx0Bgusopl6_tqumgRmAfoxHJkR74GWj_ooN62lrx8UjZQltLPvShK7bPse1xHdqRvRop-rwocIKuE3tzqMvGOFFa2Rym76Gr-f7ofjEv1TKNc_YJjqtQBzrZU3R0niD4-dbLFjYS4gF4X7DCC4DuT5HQjI5g7H2VdFNNEjC2UAUq2Xtfyr47j-VcimiBuDf7GQ9jkW8W-ec9hHlB5kk0YOfS2enTU42S5pHziJIN-3T4vq26FPWP6g1CnFFjf9VoBJQrMsZyGNv-YqpO7A_aXbTGENh1YIeLHc7ObH-ztyhMRTurJoC-94b8J2wBGkDxzWma_PIMZngQ'
}

response = requests.request("GET", url, headers=headers, data = payload).text.encode('utf8')

#print(response.text.encode('utf8'))
data=json.loads(response)
var=open('acb.csv','w')
csv.writer(var).writerow(['Type,SN'])

print(json.dumps(data,indent=4))
for i in range(len(data['response'])):
    items = data['response'][i]
    dev_type = ""
    serial_number = ""
    for key in items:

        if key=='type':
            #cbd=(key, ': ', items[key])
            dev_type = items[key]
        if key == 'serialNumber':
            serial_number = items[key]
    csv.writer(var).writerow([dev_type, serial_number])
#print(data['response'][0]["softwareVersion"])

