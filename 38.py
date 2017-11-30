class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ''
        res = '1'
        for _ in range(n-1):
            tmp, key, cnt = '', None, 0
            for s in res:
                if key == None:
                    key = s
                    cnt = 1
                elif s == key:
                    cnt += 1
                else:
                    tmp += str(cnt)
                    tmp += key
                    key = s
                    cnt = 1
            tmp += str(cnt)
            tmp += key
            res = tmp
        return res