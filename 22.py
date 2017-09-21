class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        return self.generate(n)
    
    def generate(self, n):
        """
        :rtype: list[str]
        :type n: num
        """
        if n == 0:
            return ['']
        if n == 1:
            return ['()']
        if n == 2:
            return ['()()', '(())']
        n -= 1
        res = [];
        for i in range(0, n + 1):
            j = n - i
            listi = self.generate(i)
            listj = self.generate(j)
            for strl in listi:
                for strr in listj:
                    strcurr = '(' + strl + ')' + strr
                    res.append(strcurr)
        return res

'''
括号的合法组合数量是卡特兰数
‘’‘