# 목적 : 네이버 클라우드 플랫폼 - TEXT OCR 서비스 API 사용
# 가이드 url : https://guide.ncloud-docs.com/docs/clovaocr-example01
# 파이썬보다 편리한 POSTMAN 으로 대체 권장


import requests
import uuid
import time
import json

api_url = 'InvokeURL'
secret_key = 'SECRET KEY'
image_file = 'test123.png'

request_json = {
    'images': [
        {
            'format': 'png',
            'name': 'test123'
        }
    ],
    'requestId': str(uuid.uuid4()),
    'version': 'V2',
    'timestamp': int(round(time.time() * 1000))
}

payload = {'message': json.dumps(request_json).encode('UTF-8')}
files = [
  ('file', open(image_file,'rb'))
]
headers = {
  'X-OCR-SECRET': secret_key
}

response = requests.request("POST", api_url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))


# RESPONSE 예시
"""
{
"version":"V1",
"requestId":"string",
"timestamp":1576569034247,
"images":[
  {
    "uid":"9fd73a6aacad4025b3099a36ee55aacd",
    "name":"medium","inferResult":"SUCCESS","message":"SUCCESS",
    "fields":[
        {"inferText":"나","inferConfidence":0.9967288},
        {"inferText":"하늘로","inferConfidence":0.9998919},
        {"inferText":"돌아가리라","inferConfidence":0.9999104},
        {"inferText":"아름다운","inferConfidence":0.99992156},
        {"inferText":"이","inferConfidence":0.99958915},
        {"inferText":"세상","inferConfidence":0.9998707},
        {"inferText":"소풍","inferConfidence":0.9988277},
        {"inferText":"끝내는","inferConfidence":0.9999253},
        {"inferText":"날","inferConfidence":0.99908936},
        {"inferText":"가서","inferConfidence":0.99974936},
        {"inferText":"아름다웠더라고","inferConfidence":0.9997728},
        {"inferText":"말하리라","inferConfidence":0.9993808}
        ],
    "validationResult":{"result":"NO_REQUESTED"}}
    ]
}
"""