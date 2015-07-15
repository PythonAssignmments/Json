# This file is use to parse the json which loaded using file
import os
import json

outputDir = 'output'
hxxDir = outputDir+'/hxx'
cxxDir = outputDir+'/cpp'
json_obj = {}
dict_obj = {}
lst_obj = {}
other_obj = {}

def createFiles(fileNames):
	for i in range(1, len(fileNames)):
		headerFiles = open(hxxDir+'/'+fileNames[i]+'.hxx')
		cxxFiles = open(cxxDir+'/'+fileNames[i]+'.cxx')

def writeClassInFiles(fileName, className, isNotHeader = False):
	if fileName is not None:
		fileData = ''
		if isNotHeader is True:
			fileData = '#include <iostream>\n'
			fileData = fileData + '#include \"'+className + '.hxx\"\n'
			fileData = fileData + 'using namespace std;\n'
		fileData = fileData + 'class '+ className + ' {'
		fileName.write(fileData)
		fileName.write('\n')

	else :
		print fileName,'unable to open'


def recurse_keys(df, indent = '  '):
	# ''' 
	# import json, requests, pandas
	# r = requests.post(...)  
	# rj = r.json() # json decode results query
	# j = json.dumps(rj, sort_keys=True,indent=2)            
	# df1 = pandas.read_json(j)         
	# '''
	headerFiles = ''
	cxxFiles = ''
	for key in df.keys():
		json_obj.update({str(key) : type(df[key])})

		if type(df[key]) is dict:
			headerFiles = open(hxxDir+'/'+str(key)+'.hxx','a')
			inner_dict = df[key].copy()
			dict_obj.update({type(df[key]):str(df[key])})
			writeClassInFiles(headerFiles, str(key))
			cxxFiles = open(cxxDir+'/'+str(key)+'.cxx','a')
			writeClassInFiles(cxxFiles, str(key), True)
			classMemebers = ''
			for in_key in inner_dict.keys():
				if type(inner_dict[in_key]) is int:
					classMemebers = '\tint' + ' ' + in_key + ';\n'
				if type(inner_dict[in_key]) is unicode:
					classMemebers = '\tstring' + ' ' + in_key + ';\n'
				if type(inner_dict[in_key]) is list:
					inner_lst = list()
					inner_lst = inner_dict[in_key]
					lst_len = len(inner_lst)
					classMemebers = '\t'+in_key + ' ' + str(in_key).upper() + '[' + str(lst_len) +  ']'+';\n'
				cxxFiles.write(classMemebers)


		elif type(df[key]) is list:
			headerFiles = open(hxxDir+'/'+str(key)+'.hxx','a')
			lst_obj.update({type(df[key]):str(df[key])})
			writeClassInFiles(headerFiles, str(key))
			cxxFiles = open(cxxDir+'/'+str(key)+'.cxx','a')
			writeClassInFiles(cxxFiles, str(key), True)

		if isinstance(df[key], dict):
			recurse_keys(df[key], indent+'   ')



try:
	if not os.path.exists(outputDir):
		os.mkdir(outputDir)
	if not os.path.exists(hxxDir):
		os.makedirs(hxxDir)
	if not os.path.exists(cxxDir):
		os.makedirs(cxxDir)

	with open('jsonData.json') as json_file:
		json_data = json.load(json_file)

		recurse_keys(json_data)

except:
	print "Error : File Not Found ...!!!"