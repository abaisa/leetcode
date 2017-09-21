def generateParenthesis(self, n):
    def generate(p, left, right, parens=[]):
        if left:         generate(p + '(', left-1, right)
        if right > left: generate(p + ')', left, right-1)
        if not right:    parens += p,
        return parens
    return generate('', n, n)
'''
:递归，一次生成一个符合条件的括号组
:right也为0的时候，则将生成的括号组加入结果中
:函数递归的过程中，parens参数并没有写，不影响正常使用
'''
class Solution(object):
    def generateParenthesis(self, n):
        def generate(p, left, right):
            parens=[]
            if left:         parens += generate(p + '(', left-1, right)
            if right > left: parens += generate(p + ')', left, right-1)
            if not right:    parens += p,
            return parens
        return generate('', n, n)
'''
:上面那个代码的丑陋版
:实现的东西是一样的
'''

def generateParenthesis(self, n):
    def generate(p, left, right):
        if right >= left >= 0:
            if not right:
                yield p
            for q in generate(p + '(', left-1, right): yield q
            for q in generate(p + ')', left, right-1): yield q
    return list(generate('', n, n))
'''
:这个是递归生成器的版本
:感觉意义不大，炫技用的，拿来读代码学习
'''

def generateParenthesis(self, n, open=0):
    if n > 0 <= open:
        return ['(' + p for p in self.generateParenthesis(n-1, open+1)] + \
               [')' + p for p in self.generateParenthesis(n, open-1)]
    return [')' * open] * (not n)
'''
:恐怖的一行版本
:全在返回里面，非常精炼了。慢慢看吧
'''
