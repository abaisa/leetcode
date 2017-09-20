class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dictionaryInfo = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        res = []
        for i in range(len(digits)):
            if res == []:
                res = dictionaryInfo[int(digits[i])]
            else:
                newRes = []
                for j in range(len(res)):
                    for k in range(len(dictionaryInfo[int(digits[i])])):
                        newRes.append(res[j] + dictionaryInfo[int(digits[i])][k])
                res = newRes
        return res