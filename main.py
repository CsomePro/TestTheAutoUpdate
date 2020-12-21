import time
import requests
import os

api = 'https://api.github.com/repos/CsomePro/TestTheAutoUpdate'
downloadUrl = 'https://github.com/CsomePro/TestTheAutoUpdate'
allInfo = requests.get(api).json()

print(allInfo['updated_at'])
print(time.mktime(time.strptime(allInfo['updated_at'], "%Y-%m-%dT%H:%M:%SZ")))
print(os.path.getmtime('main.py'))
name = 'main.py'
print(requests.get(downloadUrl % name))
