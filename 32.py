s = ")(()(()(((())(((((()()))((((()()(()()())())())()))()()()())(())()()(((()))))()((()))(((())()((()()())((())))(())))())((()())()()((()((())))))((()(((((()((()))(()()(())))((()))()))())"
resList = [0]
l = 1
curr= 0
for i in s:
    print(resList)
    if i == '(':
        l += 1
        if len(resList) < l:
            resList.append(resList[-1])
    elif l > 1:
        l -= 1
        curr += 2
        print('00')
        print('l = ' + str(l))
        resList[l] = max(resList[l], curr - max(resList[:l]))
    else:
        print('-------')
        curr = 0
        l = 1
print(resList)
print(max(resList))