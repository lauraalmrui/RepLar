import datetime
import os
import github
   
# If you run this example using your personal token the commit is not going to be verified.
# It only works for commits made using a token generated for a bot/app 
# during the workflow job execution.

def main(repo_token, branch):

    gh = github.Github(repo_token)

    repository = "lauraalmrui/almacenlar"

    remote_repo = gh.get_repo(repository)

    # Update files:
    #   data/example-04/latest_datetime_01.txt
    #   data/example-04/latest_datetime_02.txt
    # with the current date.

    file_to_update_01 = "/etc/passwd"
    file_to_update_02 = "/etc/passwd"

    now = datetime.datetime.now()

    file_to_update_01_content = str(now)
    file_to_update_02_content = str(now)

    blob1 = remote_repo.create_git_blob(file_to_update_01_content, "utf-8")
    element1 = github.InputGitTreeElement(
        path=file_to_update_01, mode='100644', type='blob', sha=blob1.sha)

    blob2 = remote_repo.create_git_blob(file_to_update_02_content, "utf-8")
    element2 = github.InputGitTreeElement(
        path=file_to_update_02, mode='100644', type='blob', sha=blob2.sha)

    commit_message = f'Example 04: update datetime to {now}'

    branch_sha = remote_repo.get_branch(branch).commit.sha
   
    base_tree = remote_repo.get_git_tree(sha=branch_sha)
 
    tree = remote_repo.create_git_tree([element1, element2], base_tree)

    parent = remote_repo.get_git_commit(sha=branch_sha)

    commit = remote_repo.create_git_commit(commit_message, tree, [parent])

    branch_refs = remote_repo.get_git_ref(f'heads/{branch}')

    branch_refs.edit(sha=commit.sha)
