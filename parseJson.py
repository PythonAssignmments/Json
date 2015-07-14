# This file is use to parse the json which loaded using file
import os
import json

# read the file contents
try:
	# fp = open(raw_input())
	# fileStr = fp.read()
	outputDir = 'output'
	hxxDir = outputDir+'/hxx'
	cxxDir = outputDir+'/cpp'
	if not os.path.exists(outputDir):
		os.mkdir(outputDir)
		if not os.path.exists(hxxDir):
			os.makedirs(hxxDir)
		if not os.path.exists(cxxDir):
			os.makedirs(cxxDir)
			
	with open('jsonData.json') as json_file:
		json_data = json.load(json_file)
		for data in json_data:
			# print json_data[data]
			print data
			headerFiles = open(hxxDir+'/'+data+".hxx", 'a')
			cxxFiles = open(cxxDir+'/'+data+".cxx", 'a')


		# dict1 = []
		# dict2 = {}
		# for resp_item in form_this["value"]:
		# 	dict1[resp_item]

		# print dict1
except:
	print "Error : File Not Found ...!!!"