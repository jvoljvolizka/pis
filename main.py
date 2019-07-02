#!/usr/bin/env python3
import os
import json
import sys
data=dict()
path="/home/while/Desktop/git/pis/"
def filter(text,bad=[";","\\","$","(",")",">","<","\"","'","#","&","*",",","`","?","|","{","}","%","½","^",".."]):
	c=False
	for i in bad:
		if i in text:
			print("Disabled character",i)
			sys.exit()
	return text
def save():
	j=json.dumps(data)
	f=open(path+"settings/data.json","w")
	f.write(j)
	f.close()
if  not os.path.exists(path+"settings/data.json"):
	try:
		os.mkdir("settings")
	except:
		pass
	print("Pleas create user for shh connection !")
	name=filter(input("Connection name = "))
	uname=filter(input("Username = "))
	ip = filter(input("IP = "))
	port=filter(input("Port = "))
	location=filter(input("Default transfer location = "))
	print("Username = ",uname)
	print("IP = ",ip)
	print("Completed !")
	data[name]=dict()
	data[name]['ip']=ip
	data[name]['port']=port
	data[name]['uname']=uname
	data[name]['location']=location
	save()
if data==dict():
	f=open(path+"settings/data.json")
	data=json.loads(f.read())
	f.close()
if len(sys.argv)>1:
	if "--help" in sys.argv or "-h" in sys.argv:
		print("pis")
		print("\t<connection name> ssh connection")
		print("\t--add <name>:<username>:<ip>:<port>:<location> no spaces")
		print("\t-f <connection name> <transfer file> <transfer location optional> file transfer")
	elif "--add" in sys.argv:
		i=sys.argv[2].split(":")
		filiter(i[0])
		data[i[0]]=dict()
		data[i[0]]['uname']=filter(i[1])
		data[i[0]]['ip']=filter(i[2])
		data[i[0]]['port']=filter(i[3])
		if len(i)>4:
			data[i[0]]['location']=filter(i[4])
		else:
			data[i[0]]['location']="/tmp/"
		save()
	elif "-f" in sys.argv:
		print("dosya aktarımı şeysi")
	else:
		try:
			if not sys.argv[1] in data:
				print("User not exists")
			else:
				n=filter(sys.argv[1])
				os.system(f"ssh {filter(data[n]['uname'])}@{filter(data[n]['ip'])} -p {filter(data[n]['port'])}")
		except:
			print("Pleas enter connection name !")