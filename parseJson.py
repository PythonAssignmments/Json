# This file is use to parse the json which loaded using file
import os
import json

outputDir = 'output'
hxxDir = outputDir
cxxDir = outputDir
file_lst = list()

def writeClass(fileName, className, isNotHeader = False):
	print 'writeClass()'
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
			fileData = fileData + '\n\t' + 'public :\n'
			fileData = fileData + '\n\t' + className +'() { }'
		print 'write class',className,'in',className,'.hxx file'
		fileName.write(fileData)
		fileName.write('\n')
		print 'FileData successfully write in',className,'.hxx/cxx files'

	else :
		print fileName,'unable to open'

def writeGetterSetterMethods(fileName, getterSetterMethodNames, decl = False):
	print 'writeGetterSetterMethods()'
	if fileName is not None:
		if getterSetterMethodNames is not None:
			if decl is True:
				for key in getterSetterMethodNames.keys():
					methods = ''
					print key,'=>',getterSetterMethodNames[key]
					if getterSetterMethodNames[key] is 'int':
						methods = methods + '\n\tvoid ' + 'set' + str(key)[0].upper() + str(key)[1:]+ '(int ' + str(key).lower() + '){' + '\t}\n'
						methods = methods + '\n\tint ' + 'get' + str(key)[0].upper() + str(key)[1:] + '( ){' + '\n\t\treturn ' + str(key).lower() + ';'+'\n\t}\n'
						print 'created getter/setter methods for int type'
					if getterSetterMethodNames[key] is 'unicode':
						methods = methods + '\n\tvoid ' + 'set' + str(key)[0].upper() + str(key)[1:] + '(string ' + str(key).lower() + '){' + '\t}'
						methods = methods + '\n\tstring ' + 'get' + str(key)[0].upper() + str(key)[1:] + '( ){' + '\n\t\treturn ' + str(key).lower() + ';' +'\n\t}\n'
						print 'created getter/setter methods for string type'
					if getterSetterMethodNames[key] is 'dict':
						methods = methods + '\n\tvoid ' + 'set' + str(key) + '(' + str(key) + ' '+ str(key).upper() + '){' + '\t}\n'
						methods = methods + '\n\t' + str(key) + ' ' + 'get' + str(key) + '(){' + '\n\t\treturn ' + str(key).upper() + ';'+'\n\t}\n'
						print 'created getter/setter methods for dictionary type'
					if getterSetterMethodNames[key] is 'list' :
						methods = methods + '\n\tvoid ' +  'set' + str(key) + '( ArrayList< ' + str(key) + '> ' + str(key).lower() +'List'+') {\t} \n'
						methods = methods + '\n\tArrayList<' + str(key) + '> get' + str(key) + '(){' + '\n\t\treturn ' + str(key).lower() + 'List ;' + '\n\t}'
						print 'Created getter/setter methods ArrayList'
					fileName.write(methods)
					print 'write getter/setter methods defination in',fileName
			else :
				for key in getterSetterMethodNames.keys():
					methods = ''
					print key,'=>',getterSetterMethodNames[key]
					if getterSetterMethodNames[key] is 'int':
						methods = methods + '\n\tvoid ' + 'set' + str(key)[0].upper() + str(key)[1:]+ '(int ' + str(key).lower() + ');\n'
						methods = methods + '\n\tint ' + 'get' + str(key)[0].upper() + str(key)[1:] + '( );\n'
						print 'created getter/setter methods for int type'
					if getterSetterMethodNames[key] is 'unicode':
						methods = methods + '\n\tvoid ' + 'set' + str(key)[0].upper() + str(key)[1:] + '(string ' + str(key).lower() + ');\n'
						methods = methods + '\n\tstring ' + 'get' + str(key)[0].upper() + str(key)[1:] + '( );\n'
						print 'created getter/setter methods for string type'
					if getterSetterMethodNames[key] is 'dict':
						methods = methods + '\n\tvoid ' + 'set' + str(key) + '(' + str(key) + ' '+ str(key).upper() + ');\n'
						methods = methods + '\n\t' + str(key) + ' ' + 'get' + str(key) + '( );\n'
						print 'created getter/setter methods for dictionary type'
					if getterSetterMethodNames[key] is 'list':
						methods = methods + '\n\tvoid ' + 'set' + str(key) + '( ArrayList<' + str(key) + '> ' + str(key).lower() + 'List' + ' );\n'
						methods = methods + '\n\tArrayList<' + str(key) + '> ' + 'get' + str(key) + '();\n'
 					fileName.write(methods)
					print 'write getter/setter methods declaration in',fileName

# def writeClassDataMembers(inner_dict):

def traverseParseJson(df):
	print 'traverseParseJson()'
	getterSetter_dict = {}
	headerFiles = ''
	cxxFiles = ''
	for key in df.keys():
		if type(df[key]) is dict:
			headerFiles = open(hxxDir+'/'+str(key)+'.hxx','a')
			file_lst.append(headerFiles)
			print headerFiles,'is created.'
			inner_dict = df[key].copy()
			writeClass(headerFiles, str(key), False)
			cxxFiles = open(cxxDir+'/'+str(key)+'.cxx','a')
			file_lst.append(cxxFiles)
			print cxxFiles,'is created.'
			writeClass(cxxFiles, str(key), True)
			classMemebers = ''
			for in_key in inner_dict.keys():
				getterSetter_dict = {}
				if type(inner_dict[in_key]) is int:
					classMemebers = '\n\tint' + ' ' + in_key + ';\n'
					getterSetter_dict.update({in_key : 'int'})
				if type(inner_dict[in_key]) is unicode:
					classMemebers = '\n\tstring' + ' ' + in_key + ';\n'
					getterSetter_dict.update({in_key : 'unicode'})
				if type(inner_dict[in_key]) is list:
					inner_lst = list()
					inner_lst = inner_dict[in_key]
					lst_len = len(inner_lst)
					classMemebers = '\n\t'+ 'ArrayList <'+ in_key + '>' +' ' + str(in_key).lower() + 'List'+';\n'
					getterSetter_dict.update({in_key:'list'})
				if type(inner_dict[in_key]) is dict:
					classMemebers = '\n\t' + in_key + ' ' + in_key.upper() + ';\n'
					getterSetter_dict.update({in_key:'dict'})
				headerFiles.write(classMemebers)
				cxxFiles.write(classMemebers)
				writeGetterSetterMethods(headerFiles, getterSetter_dict, False)
				writeGetterSetterMethods(cxxFiles, getterSetter_dict, True)

		elif type(df[key]) is list:
			headerFiles = open(hxxDir+'/'+str(key)+'.hxx','a')
			file_lst.append(headerFiles)
			writeClass(headerFiles, str(key))
			cxxFiles = open(cxxDir+'/'+str(key)+'.cxx','a')
			file_lst.append(cxxFiles)
			writeClass(cxxFiles, str(key), True)
			inner_lst = list()
			inner_lst = df[key]

			try:
				if len(inner_lst) > 0 :
					for i in range(0, 1):
						if isinstance((inner_lst[i]), dict):
							inner_dictionary = inner_lst[i].copy()
							traverseParseJson(inner_lst[i])
							classMemebers1 = ''
							inner_dict1 = inner_lst[i].copy()
							for inn_key in inner_dict1.keys():
								getterSetter_dict = {}
								print '+++++',inn_key,'=>',type(inner_dict1[inn_key])
								if type(inner_dict1[inn_key]) is int:
									classMemebers1 = '\n\tint' + ' ' + inn_key + ';\n'
									getterSetter_dict.update({inn_key:'int'})
								if type(inner_dict1[inn_key]) is unicode:
									classMemebers1 = '\n\tstring' + ' ' + inn_key + ';\n'
									getterSetter_dict.update({inn_key : 'unicode'})
								if type(inner_dict1[inn_key]) is dict:
									classMemebers1 = '\n\t' + inn_key + ' ' + inn_key.upper() + ';\n'
									getterSetter_dict.update({inn_key:'dict'})
								headerFiles.write(classMemebers1)
								cxxFiles.write(classMemebers1)
								writeGetterSetterMethods(headerFiles, getterSetter_dict, False)
								writeGetterSetterMethods(cxxFiles, getterSetter_dict, True)
			except:
				print 'list size is less than 0'

		if isinstance(df[key], dict):
			traverseParseJson(df[key])


def closeAllFiles(fileNames):
	if fileNames is not None:
		for i in range(0, len(fileNames)):
			fileNames[i].write('\n };')
			fileNames[i].close()

try:
	# make the output directory to store cxx and hxx files
	if not os.path.exists(outputDir):
		os.mkdir(outputDir)

	with open('jsonSampleData/jsonData.json') as json_file:
		# Deserialize the json instances into the python objects
		json_data = json.load(json_file)
		if json_data is not None:
			# Traverse the json, so that get inner python objects
			traverseParseJson(json_data)
			# Close all open files
			closeAllFiles(file_lst)
			print 'files created successfully !!!!'
		else:
			print json_file,'contents invalid JSON !!!'

except:
	print "Error : File Not Found ...!!!"
