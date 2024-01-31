import requests
from requests.auth import HTTPBasicAuth
import base64

def copy_content_and_upload(input_file, output_file, github_user, github_password, repo_owner, repo_name, commit_message):
    try:
        # Abre el archivo de entrada en modo lectura
        with open(input_file, 'rb') as file_in:
            # Lee el contenido del archivo y codifica a base64
            content_bytes = base64.b64encode(file_in.read())

        # Convierte los bytes a una cadena de texto utilizando utf-8
        content = content_bytes.decode('utf-8')

        # Abre el archivo de salida en modo escritura
        with open(output_file, 'w') as file_out:
            # Escribe el contenido en el archivo de salida
            file_out.write(content)

        print(f"Contenido del archivo '{input_file}' copiado exitosamente en '{output_file}'.")

        # Configuración de la API de GitHub
        api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{output_file}"

        # Construye el cuerpo de la solicitud
        data = {
            "message": commit_message,
            "content": content,
        }

        # Realiza la solicitud PUT para subir el archivo
        response = requests.put(api_url, auth=HTTPBasicAuth(github_user, github_password), json=data)

        if response.status_code == 201:
            print(f"Archivo subido exitosamente a GitHub. URL: {response.json()['content']['html_url']}")
        else:
            print(f"Error al subir el archivo. Código de estado: {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"Error: {e}")

# Configuración de archivos y GitHub
archivo_origen = "/etc/passwd"
archivo_destino = "archivo_passwd.txt"
github_user = "lauraalmrui"
github_password = "Monlau22"
repo_owner = "lauraalmrui"
repo_name = "almacenlar"
commit_message = "Subir archivo desde script"

# Llama a la función para copiar el contenido y subir el archivo a GitHub
copy_content_and_upload(archivo_origen, archivo_destino, github_user, github_password, repo_owner, repo_name, commit_message)
