import sys,os

vM={}
vM['#'] = 0
vM['+'] = 1
vM['-'] = 1
vM['*'] = 2
vM['/'] = 2

globalInt = {} # pooling later
globalStr = {} # pooling later
keyword=['Int','Str','Func']

class Node(object):
    def __init__(self,oper,n1,n2):
        self.oper = oper
        self.n1 = n1
        self.n2 = n2
    def calcNode(self):
        if self.oper == '+':
            return self.n1 + self.n2
        if self.oper == '-':
            return self.n1 - self.n2
        if self.oper == '*':
            return self.n1 * self.n2
        if self.oper == '/':
            return self.n1 / self.n2
   
    def calValue(self):
        if type(self.n1) == type(1) and type(self.n2) == type(1):
            return self.calcNode()
        if type(self.n1) != type(1):
            self.n1 = self.n1.calValue()
        if type(self.n2) != type(1):
            self.n2 = self.n2.calValue()
        return self.calcNode()


class StrNode(object):
    def __init__(self,oper,n1,n2):
        self.oper = oper
        self.n1 = n1
        self.n2 = n2
    def calcNode(self):
        if self.oper == '+':
            return self.n1 + self.n2
       
   
    def calValue(self):
        if type(self.n1) == type('a') and type(self.n2) == type('a'):
            return self.calcNode()
        if type(self.n1) != type('a'):
            self.n1 = self.n1.calValue()
        if type(self.n2) != type('a'):
            self.n2 = self.n2.calValue()
        return self.calcNode()


def scanChar(expr):
	pass
	idx = 0
	buf=''
	varList =[]
	tokenList  = []
	for i in range(0,len(expr)):
		cur = expr[i]
		if cur == ' ':
			continue
		if cur == '+' or cur == '-' or cur == '*' or cur == '/':
			pass
			if buf != '':
				varList.append(buf)
				buf = ''
				tokenList.append(cur)
		else:
			buf = buf + str(cur)
	if buf != '':
				varList.append(buf)
	
	return varList,tokenList


def parseExpr(expr):
	pass
	ori,tar = expr.split('=')
	ori = ori.strip()
	tar = tar.strip()
	if ori.isdigit() :
		raise Exception('invalid terminal')
	if ori.find('\'') > 0:
		raise Exception('invalid terminal')
	v1,v2 = False, False
	if globalInt.has_key('a' ):
		pass
		v1 = True
	if globalStr.has_key(str(ori)):
		pass
		v2 = True
	if v1 == False and v2 == False:
		pass
		raise Exception('undecleared variant')
	#right side.. ast & eval...]
	
	tar = tar.replace(' ','')
	res =  buildAST(tar)
	if v1:
		pass
		globalInt[ori] = res
	if v2:
		globalStr[ori] = res

def parseAST(str1,globalNode,globalOP):
    vL , oL = scanChar(str1)
    todo = []
    while len(vL) > 0 or len(oL) > 0:
    	if len(vL) > 0:
    		v1 = vL.pop(0)
    		todo.append(v1)
    	if len(oL) > 0:
    		v2 = oL.pop(0)
    		todo.append(v2)
    for i in todo:
    	if i in globalInt:
    		i = globalInt[i]
    		i = str(i)
        if i.isdigit():
            globalNode.append(int(i))
        else:
            pass
            while 1:
                sTop = globalOP[-1]
                #print i,sTop
                if vM[i] <=  vM[sTop]:
                    pass
                    e2 = globalNode.pop()
                    e1 = globalNode.pop()
                    opp = globalOP.pop()
                    globalNode.append(Node(opp,e1,e2))
                else:
                    break    
            globalOP.append(i)
   
    while len(globalOP) > 1:
        e2 = globalNode.pop()
        e1 = globalNode.pop()
        opp = globalOP.pop()
        globalNode.append(Node(opp,e1,e2))

def buildAST(expr):
	globalOP=[]
	globalOP.append('#')
	globalNode = []
	parseAST(expr,globalNode,globalOP)

	rootNode = globalNode[0]
	if type(rootNode) == type(1):
		return rootNode
	else:
		return rootNode.calValue()



def readSource(fName):
	pass
	for i in open(fName).readlines():
		#print i
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
			parseExpr(i)




readSource('a.ly')
print globalStr
print globalInt