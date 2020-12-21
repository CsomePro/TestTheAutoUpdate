import time
import requests
import os
import zipfile


def update_file():
    # 下载zip文件
    downloadUrl = 'https://github.com/CsomePro/TestTheAutoUpdate/archive/master.zip'
    print('正在下载文件...')
    with open('tmp.zip', 'wb') as f:
        f.write(requests.get(downloadUrl).content)
    # 解压zip文件
    zipFile = zipfile.ZipFile('tmp.zip')
    zipList = zipFile.namelist()
    # print(zipList)
    # abspath = os.path.dirname(os.path.abspath(__file__))
    # print(os.path.dirname(os.path.abspath(__file__)))
    zipFile.extract('TestTheAutoUpdate-master/main.py')
    zipFile.close()

    # 复制文件
    print('正在替换文件...')
    with open('TestTheAutoUpdate-master/main.py', 'rb') as source:
        with open('main.py', 'wb') as destination:
            destination.write(source.read())

    # 删除文件
    os.remove('tmp.zip')
    os.remove('TestTheAutoUpdate-master/main.py')
    os.rmdir('TestTheAutoUpdate-master')

    print('更新成功！')


api = 'https://api.github.com/repos/CsomePro/TestTheAutoUpdate'
allInfo = requests.get(api).json()
new_time = time.mktime(time.strptime(allInfo['updated_at'], "%Y-%m-%dT%H:%M:%SZ"))
file_time = os.path.getmtime('main.py')
if new_time > file_time:
    print("updating")
    update_file()

print("update")