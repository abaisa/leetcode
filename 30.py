class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        index = 0
        aWordLen = len(words[0])
        wordCount = len(words)
        allLen = len(words) * len(words[0])
        strLen = len(s)
        res = []
        while (index + allLen) <= strLen:
            xList = []
            addFlag = True
            for word in words:
                flag = False
                for x in range(wordCount):
                    if s[index+x*aWordLen:index+(x+1)*aWordLen] == word and x not in xList:
                        flag = True
                        xList.append(x)
                        break
                if not flag:
                    addFlag = False
                    break
            if addFlag:
                res.append(index)
            index += 1
        return res