#!/usr/bin/env python3

import os
import json
import sys
data=dict()
path="/home/while/Desktop/git/pis/"
def save():
	j=json.dumps(data)
	f=open(path+"settings/data.json","w")
	f.write(j)
	f.close()
if  not os.path.exists(path+"settings/data.json"):
	os.mkdir("settings")
	print("Pleas create user for shh connection !")
	name=input("Connection name = ")
	uname=input("Username = ")
	ip = input("IP = ")
	port=input("Port = ")
	location=input("Default transfer location = ")
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
		data[i[0]]=dict()
		data[i[0]]['ip']=i[1]
		data[i[0]]['port']=i[2]
		data[i[0]]['uname']=i[3]
		if len(i)>4:
			data[i[0]]['location']=i[4]
		else:
			data[i[0]]['location']="/tmp/"
		save()
	elif "-f" in sys.argv:
		print("dosya aktarımı şeysi")
	else:
		try:
			print(sys.argv[1])
			if not sys.argv[1] in data:
				print("User not exists")
		except:
			print("Pleas enter connection name !")