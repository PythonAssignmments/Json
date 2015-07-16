# This file is use to parse the json which loaded using file
import os
import json

outputDir = 'output'
hxxDir = outputDir+'/hxx'
cxxDir = outputDir+'/cpp'
file_lst = list()

def writeClassInFiles(fileName, className, isNotHeader = False):
	print 'writeClassInFiles()'
	if fileName is not None:
		fileData = ''
		if isNotHeader is True:
			fileData = '#include <iostream>\n'
			fileData = fileData + '#include \"'+ hxxDir +'/'+className + '.hxx\"\n'
			fileData = fileData + 'using namespace std;\n'
			fileData = fileData + 'class '+ className + ' {'
			print 'write #include... in',className,'.cxx files'
		else:
			fileData = 'class '+ className + '{'
			fileData = fileData + '\n\t' + className +'() { }'
		print 'write class',className,'in',className,'.hxx file'
		fileName.write(fileData)
		fileName.write('\n')

	else :
		print fileName,'unable to open'

def writeGetterSetterMethods(fileName, getterSetterMethodNames):
	print 'writeGetterSetterMethods()'
	if fileName is not None:
		for key in getterSetterMethodNames.keys():
			methods = ''
			print key,'=>',getterSetterMethodNames[key]
			if getterSetterMethodNames[key] is 'int':
				methods = methods + '\n\tvoid ' + 'set' + str(key).upper() + '(int ' + str(key).lower() + '){' + '\t}'
				methods = methods + '\n\tint ' + 'get' + str(key).upper() + '( ){' + '\n\t\treturn ' + str(key).lower() + '\n\t}'
				print 'created getter/setter methods for int type'
			if getterSetterMethodNames[key] is 'unicode':
				methods = methods + '\n\tvoid ' + 'set' + str(key).upper() + '(string ' + str(key).lower() + '){' + '\t}'
				methods = methods + '\n\tstring ' + 'get' + str(key).upper() + '( ){' + '\n\t\treturn ' + str(key).lower() + '\n\t}'
				print 'created getter/setter methods for string type'
			fileName.write(methods)
			print 'write getter/setter methods in',fileName




def recurse_keys(df, indent = '  '):
	# ''' 
	# import json, requests, pandas
	# r = requests.post(...)  
	# rj = r.json() # json decode results query
	# j = json.dumps(rj, sort_keys=True,indent=2)            
	# df1 = pandas.read_json(j)         
	# '''
	print 'recurse_keys()'
	getterSetter_dict = {}
	headerFiles = ''
	cxxFiles = ''
	for key in df.keys():
		# json_obj.update({str(key) : type(df[key])})
		print key,'->',type(df[key])
		if type(df[key]) is dict:
			headerFiles = open(hxxDir+'/'+str(key)+'.hxx','a')
			file_lst.append(headerFiles)
			print headerFiles,'is created.'
			inner_dict = df[key].copy()
			writeClassInFiles(headerFiles, str(key), False)
			cxxFiles = open(cxxDir+'/'+str(key)+'.cxx','a')
			file_lst.append(cxxFiles)
			print cxxFiles,'is created.'
			writeClassInFiles(cxxFiles, str(key), True)
			classMemebers = ''
			for in_key in inner_dict.keys():
				getterSetter_dict = {}
				if type(inner_dict[in_key]) is int:
					classMemebers = '\n\tint' + ' ' + in_key + ';\n'
					# cxxFiles.write(classMemebers)
					getterSetter_dict.update({in_key : 'int'})
				if type(inner_dict[in_key]) is unicode:
					classMemebers = '\n\tstring' + ' ' + in_key + ';\n'
					# cxxFiles.write(classMemebers)
					getterSetter_dict.update({in_key : 'unicode'})
				if type(inner_dict[in_key]) is list:
					inner_lst = list()
					inner_lst = inner_dict[in_key]
					lst_len = len(inner_lst)
					classMemebers = '\n\t'+in_key + ' ' + str(in_key).upper() + '[' + str(lst_len) +  ']'+';\n'
				cxxFiles.write(classMemebers)
				writeGetterSetterMethods(cxxFiles, getterSetter_dict)
				# cxxFiles.write(classMemebers)

		elif type(df[key]) is list:
			headerFiles = open(hxxDir+'/'+str(key)+'.hxx','a')
			file_lst.append(headerFiles)
			writeClassInFiles(headerFiles, str(key))
			cxxFiles = open(cxxDir+'/'+str(key)+'.cxx','a')
			file_lst.append(cxxFiles)
			writeClassInFiles(cxxFiles, str(key), True)
			inner_lst = list()
			inner_lst = df[key]

			for i in range(0, 1):
				if isinstance((inner_lst[i]), dict):
					recurse_keys(inner_lst[i], indent+'   ')
					classMemebers1 = ''
					inner_dict1 = inner_lst[i].copy()
					for inn_key in inner_dict1.keys():
						print inn_key
						if type(inner_dict1[inn_key]) is int:
							classMemebers1 = '\n\tint' + ' ' + inn_key + ';\n'
						if type(inner_dict1[inn_key]) is unicode:
							classMemebers1 = '\n\tstring' + ' ' + inn_key + ';\n'
						cxxFiles.write(classMemebers1)

		if isinstance(df[key], dict):
			recurse_keys(df[key], indent+'   ')


def closeAllFiles(fileNames):
	if fileNames is not None:
		for i in range(0, len(fileNames)):
			fileNames[i].write('\n };')
			fileNames[i].close()

try:
	if not os.path.exists(outputDir):
		os.mkdir(outputDir)
	if not os.path.exists(hxxDir):
		os.makedirs(hxxDir)
	if not os.path.exists(cxxDir):
		os.makedirs(cxxDir)

	with open('jsonData.json') as json_file:
		json_data = json.load(json_file)
		if json_data is not None:
			recurse_keys(json_data)
			# for i in range(0, len(file_lst)):
			# 	print file_lst[i]
			closeAllFiles(file_lst)
		else:
			print json_file,'contents invalid JSON !!!'

except:
	print "Error : File Not Found ...!!!"