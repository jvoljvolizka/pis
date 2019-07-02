#!/usr/bin/env python3

import os
import json
import sys
data=dict()
if  not os.path.exists("settings/data.json"):
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
	j=json.dumps(data)
	f=open("settings/data.json","w")
	f.write(j)
	f.close()
if data==dict():
	f=open("settings/data.json")
	data=json.loads(f.read())
	f.close()
if len(sys.argv)>1:
	if "--help" in sys.argv or "-h" in sys.argv:
		print("pis")
		print("-c -n <connection name> ssh connection")
		print("-c --name <connection name> ssh connection")
		print("--add <name>:<username>:<ip>:port no spaces")
		print("-f <connection name> <transfer file> <transfer location optional> file transfer")
	elif "-c" in sys.argv:
		if "-n" in sys.argv or "--name" in sys.argv:
			print(sys.argv[3])
	elif "--add" in sys.argv:
		i=sys.argv[2].split(":")
		data[i[0]]=dict()
		data[i[0]]['ip']=i[1]
		data[i[0]]['port']=i[2]
		data[i[0]]['uname']=i[3]
		data[i[0]]['location']=i[4]
	elif "-f" in sys.argv:
		print("dosya aktarımı şeysi")