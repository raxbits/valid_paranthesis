def sol1(arr:str) -> bool:
'''
handles single paranthesis character type.
t -> o(n)
s -> o(1)
'''

	cnt = 0
	for i in arr:
		if i == ')':
			cnt -=1
		elif i == '(':
			cnt+=1
		elif cnt < 0:
			return False
	if cnt > 0:
		return False
	return True

