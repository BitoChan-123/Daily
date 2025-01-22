import urllib, urllib3, sys, uuid
import ssl
import sys
import io

# 强制设置标准输出为 UTF-8
def print_utf8(text):
    sys.stdout.write(text.encode('utf-8').decode('utf-8'))



host = 'https://ali-market-tongue-detect-v2.macrocura.com'
path = '/diagnose/face-tongue/result/'
method = 'POST'
appcode = '9924ed728c734d3f90405aa5e192fa87'
querys = ''
bodys = {}
url = host + path

http = urllib3.PoolManager()
headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': 'APPCODE ' + appcode
}
bodys[''] = "{\"scene\":1,\"tf_image\":\"https://www.cdstm.cn/gallery/media/mkjx/xgbnysdw_6453/202101/W020210125763567472790.jpg\"}"
post_data = bodys['']
response = http.request('POST', url, body=post_data, headers=headers)
content = response.data.decode('utf-8')
if (content):
    print_utf8(content)