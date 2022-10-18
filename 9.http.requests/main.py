import requests

token = 'y0_AgAAAAACXMR-AADLWwAAAADRksHhjUlzKnB1TxKLv4XpEKnTULadczg'
host = 'https://cloud-api.yandex.net:443'
url = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Authorization': f'OAuth {token}'}
path = 'test'
print(requests.put(f'{host}?path={path}', headers=headers))
