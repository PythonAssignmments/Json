# This file is use to parse the json which loaded using file
import os
import json

file_lst = list()
objAndFiles = {}


def writeClass(fileName, className, isNotHeader, root):
	print 'writeClass()'
	if fileName is not None:
		fileData = ''
		if isNotHeader is True:
			fileData = '#include <iostream>\n'
			fileData = fileData + '#include \"' + root + '/'+className + '.hxx\"\n'
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

	else :
		print fileName,'unable to open'

def writeGetterSetterMethods(fileName, getterSetterMethodNames, defination = False):
	print 'writeGetterSetterMethods()'
	if fileName is not None:
		if getterSetterMethodNames is not None:
			if defination is True:
				for key in getterSetterMethodNames.keys():
					methods = ''
					print key,'=>',getterSetterMethodNames[key]
					if getterSetterMethodNames[key] is 'int':
						methods = methods + '\n\tvoid ' + 'set' + str(key)[0].upper() + str(key)[1:]+ '(int ' + str(key).lower() + '){' + '\t}\n'
						methods = methods + '\n\tint ' + 'get' + str(key)[0].upper() + str(key)[1:] + '(){' + '\n\t\treturn ' + str(key).lower() + ';'+'\n\t}\n'
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
					if getterSetterMethodNames[key] is 'bool':
						methods = methods + '\n\tvoid ' + 'set' + str(key)[0].upper() + str(key)[1:] + '(bool '+ str(key)+'){\t}\n' 
						methods = methods + '\n\tbool ' + 'get' + str(key)[0].upper() + str(key)[1:] + '(){\n\t\treturn ' + str(key) + ';'+ '\n\t}\n'
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
					if getterSetterMethodNames[key] is 'bool':
						methods = methods + '\n\tvoid ' + 'set' + str(key)[0].upper() + str(key)[1:] + '(bool ' + str(key) + ');\n'
						methods = methods + '\n\tbool ' + 'get' + str(key)[0].upper() + str(key)[1:] + '();\n'
 					fileName.write(methods)
					print 'write getter/setter methods declaration in',fileName


def writeClassMembers(inner_dict, headerFiles, cxxFiles):
	classMemebers = ''
	if inner_dict is not None:
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
				objAndFiles.update({str(in_key):headerFiles})
			if type(inner_dict[in_key]) is dict:
				classMemebers = '\n\t' + in_key + ' ' + in_key.upper() + ';\n'
				getterSetter_dict.update({in_key:'dict'})
			if type(inner_dict[in_key]) is bool:
				classMemebers = '\n\tbool ' + in_key + ';\n'
				getterSetter_dict.update({in_key:'bool'})
			headerFiles.write(classMemebers)
			cxxFiles.write(classMemebers)
			writeGetterSetterMethods(headerFiles, getterSetter_dict, False)
			writeGetterSetterMethods(cxxFiles, getterSetter_dict, True)



def traverseParseJson(df, root):
	print 'traverseParseJson()'
	getterSetter_dict = {}
	headerFiles = ''
	cxxFiles = ''
	for key in df.keys():
		if type(df[key]) is dict:
			headerFiles = open(root+'/'+str(key)+'.hxx','w+')
			file_lst.append(headerFiles)
			print file_lst
			print 'file open'
			print headerFiles,'is created.'
			inner_dict = df[key].copy()
			writeClass(headerFiles, str(key), False, root)
			cxxFiles = open(root+'/'+str(key)+'.cxx','w+')
			file_lst.append(cxxFiles)
			print cxxFiles,'is created.'
			writeClass(cxxFiles, str(key), True, root)
			writeClassMembers(inner_dict, headerFiles, cxxFiles)

		elif type(df[key]) is list:
			headerFiles = open(root+'/'+str(key)+'.hxx','w+')
			file_lst.append(headerFiles)
			writeClass(headerFiles, str(key), False, root)
			cxxFiles = open(root+'/'+str(key)+'.cxx','w+')
			file_lst.append(cxxFiles)
			writeClass(cxxFiles, str(key), True, root)
			inner_lst = list()
			inner_lst = df[key]

			try:
				if len(inner_lst) > 0 :
					for i in range(0, 1):
						if isinstance((inner_lst[i]), dict):
							inner_dictionary = inner_lst[i].copy()
							traverseParseJson(inner_lst[i], root)
							inner_dict1 = inner_lst[i].copy()
							writeClassMembers(inner_dict1, headerFiles, cxxFiles)

			except:
				print 'list size is less than 0'

		if isinstance(df[key], dict):
			traverseParseJson(df[key], root)


def closeAllFiles(fileNames):
	if fileNames is not None:
		for i in range(0, len(fileNames)):
			print fileNames[i],'=>',len(fileNames)
			fileNames[i].write('\n };')
			fileNames[i].close()
			print fileNames[i],' closed'

def writeRelativeHeaderFiles(headerFiles, root):
	if headerFiles is not None:
		for key in headerFiles.keys():
			try :
				print headerFiles[key].name
				with open(headerFiles[key].name,'r+') as fp1:
					strH = '#include \"' + root + '/'+key + '.hxx\"\n'
					oldData = fp1.read()
					fp1.seek(0)
					fp1.write(strH + oldData)
					fp1.close()
			except:
				print "Failed to open ", headerFiles[key]

	else :
		print 'Empty dictionary'

try:

	for root, dirs, files in os.walk(raw_input("Enter Directory name:")):
		for fileName in files:
			if fileName.endswith('.json'):
				filePath = os.path.join(root, fileName)
				print root
				with open(filePath) as json_file:
					print json_file
				# Deserialize the json instances into the python objects
					json_data = json.load(json_file)
					if json_data is not None:
						# Traverse the json, so that get inner python objects
						traverseParseJson(json_data, root)
						# Close all open files
						closeAllFiles(file_lst)
						# include header file in relative header file
						writeRelativeHeaderFiles(objAndFiles, root)
						print ' files created successfully !!!!'
						file_lst = []
					else:
							print 'contents invalid JSON !!!'

except Exception, err:
	print Exception, err
