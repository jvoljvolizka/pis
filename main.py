#!/usr/bin/env python3

import os
import json
data=dict()
if  not os.path.exists("settings/data.json"):
	os.mkdir("settings")
	print("Pleas create user for shh connection !")
	name=input("Connection name = ")
	uname=input("Username = ")
	ip = input("IP = ")
	location=input("Default transfer location = ")
	print("Username = ",uname)
	print("IP = ",ip)
	
	print("Completed !")
	data[name]=dict()
	data[name]['ip']=ip
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
print(data)