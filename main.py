import time
import requests
import os
import zipfile

url = 'https://github.com/CsomePro/TestTheAutoUpdate/archive/master.zip'
objectn = 'TestTheAutoUpdate-master'
dest = 'main.py'


def update_file(downloadUrl, objectName, targetFile):
    # 下载zip文件
    mainFile = objectName + "-master/" + targetFile
    print('正在下载文件...')
    with open('tmp.zip', 'wb') as f:
        f.write(requests.get(downloadUrl).content)
    # 解压zip文件
    zipFile = zipfile.ZipFile('tmp.zip')
    zipList = zipFile.namelist()
    # print(zipList)
    # abspath = os.path.dirname(os.path.abspath(__file__))
    # print(os.path.dirname(os.path.abspath(__file__)))
    zipFile.extract(mainFile)
    zipFile.close()

    # 复制文件
    print('正在替换文件...')
    with open(mainFile, 'rb') as source:
        with open(targetFile, 'wb') as destination:
            destination.write(source.read())

    # 删除文件
    os.remove('tmp.zip')
    os.remove(mainFile)
    os.rmdir(os.path.dirname(mainFile))

    print('更新成功！')


api = 'https://api.github.com/repos/CsomePro/TestTheAutoUpdate'
allInfo = requests.get(api).json()
new_time = time.mktime(time.strptime(allInfo['updated_at'], "%Y-%m-%dT%H:%M:%SZ"))
file_time = os.path.getmtime('main.py') - 28800
print(new_time)
print(file_time)
if new_time > file_time:
    print("updating")
    update_file(url, objectn, dest)

print("update")
os.system('pause')
