s = 'asdfghjkl'
for i in range(9):
	s = str(s[:i]) + str(i+1) + str(s[i+1:])
	print(s)