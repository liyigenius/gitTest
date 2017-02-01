import sys,os

globalInt = {} # pooling later
globalStr = {} # pooling later
keyword=['Int','Str','Func']
def readSource(fName):
	pass
	for i in open(fName).readlines():
		print i
		i=i.replace(';','')
		tokens = i.split()
		if len(tokens) > 1 :
			if tokens[0] == 'Int':
				#add to pool...
				globalInt[tokens[1]] = 0
			if tokens[0] == 'Str':
				globalStr[tokens[1]] = ''

		if i.find('=') >= 0:
			#parse expr...


readSource('a.ly')
print globalStr
print globalInt