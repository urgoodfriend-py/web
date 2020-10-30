import os
import sys
import requests
from urllib.request import urlopen
import json 

def judgment(imgurl):
    client_id = "tz5oef8zdq"
    client_secret = "JVwWZdVw5NUwKQGSZnRzdiNzvAdAK0Ci21roDIVA"
    url = "https://naveropenapi.apigw.ntruss.com/vision/v1/celebrity" # 유명인 얼굴인식

    img = urlopen(imgurl).read()
    files = {'image': img}
    # files = {'image': open('aaa.jpeg', 'rb')}
    headers = {'X-NCP-APIGW-API-KEY-ID': client_id, 'X-NCP-APIGW-API-KEY': client_secret }
    response = requests.post(url,  files=files, headers=headers)
    rescode = response.status_code
    if(rescode==200): # ok라는 응답
        print(response.text)
        json_dic = json.loads(response.text)
        # print(json_dic.get('faces')[0].get('celebrity').get('value'))
        return json_dic.get('faces')[0].get('celebrity').get('value')
    else:
        print("Error Code:" + rescode)
