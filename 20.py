class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = []
        for k in range(int(len(s))):
            i = s[k]
            if i == '(':
                l.append('(')
            elif i == '[':
                l.append('[')
            elif i == '{':
                l.append('{')
            elif i == ')':
                if(len(l) > 0 and l[-1] == '('):
                    l.pop()
                else:
                    return False
            elif i == ']':
                if(len(l) > 0 and l[-1] == '['):
                    l.pop()
                else:
                    return False
            elif i == '}':
                if(len(l) > 0 and l[-1] == '{'):
                    l.pop()
                else:
                    return False
        if(len(l) == 0):
            return True
        return False