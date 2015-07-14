# This file is use to parse the json which loaded using file
import json

# read the file contents
try:
	# fp = open(raw_input())
	# fileStr = fp.read()
	with open('jsonData.json') as json_file:
		json_data = json.load(json_file)
		for data in json_data:
			print data

		for data1 in data[1]:
			print data1
		# dict1 = []
		# dict2 = {}
		# for resp_item in form_this["value"]:
		# 	dict1[resp_item]

		# print dict1
except:
	print "Error : File Not Found ...!!!"