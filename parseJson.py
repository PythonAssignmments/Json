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
		if isNotHeader is True :
			fileData = '#include \"'+className + '.hxx\"\n'
		fileData = fileData + 'class'+ className + ' {'
		fileName.write(fileData)

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
		headerFiles = open(hxxDir+'/'+str(key)+'.hxx','a')

		json_obj.update({str(key) : type(df[key])})

		if type(df[key]) == dict:
			inner_dict = df[key].copy()
			dict_obj.update({type(df[key]):str(df[key])})
			writeClassInFiles(headerFiles, str(key))
			cxxFiles = open(cxxDir+'/'+str(key)+'.cxx','a')
			writeClassInFiles(cxxFiles, str(key), True)

			for key in inner_dict.keys():
				print key,'->',inner_dict[key]

		elif type(df[key]) == list:
			headerFiles = open(hxxDir+'/'+str(key)+'.hxx','a')
			lst_obj.update({type(df[key]):str(df[key])})
			writeClassInFiles(headerFiles, str(key))
			cxxFiles = open(cxxDir+'/'+str(key)+'.cxx','a')
			writeClassInFiles(cxxFiles, str(key), True)
			# if headerFiles is not None :
			# 	writeClassInFiles(headerFiles, str(key), False, other_obj)
			
			# if cxxFiles is not None:
			# 	writeClassInFiles(cxxFiles, str(key), True, other_obj)



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
		# if json_obj is not None:
		# 	for key, val in json_obj.items():
		# 		print key,'->',val

except:
	print "Error : File Not Found ...!!!"