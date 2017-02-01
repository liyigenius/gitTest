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

print scanChar('1')