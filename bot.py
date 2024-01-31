from github import Github

# Definir la variable GITHUB_REPO
GITHUB_REPO = 'almacenlar'

g = Github("lauraalmrui", "Monlau22")

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
git_file = git_prefix + '/etc/passwd'
if git_file in all_files:
    contents = repo.get_contents(git_file)
    repo.update_file(contents.path, "committing files", content, contents.sha, branch="master")
    print(git_file + ' UPDATED')
else:
    repo.create_file(git_file, "committing files", content, branch="master")
    print(git_file + ' CREATED')
