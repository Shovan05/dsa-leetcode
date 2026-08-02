class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        lst = s.split()
        if len(lst)!=len(pattern):
            return False
        charToWord={}
        wordToChar={}

        for i in range (len(lst)):

            ch=pattern[i]
            word=lst[i]

            if word not in wordToChar:
                wordToChar[word]=ch
            else:
                if wordToChar[word]!=ch:
                    return False

            if ch not in charToWord:
                charToWord[ch]=word
            else:
                if charToWord[ch]!=word:
                    return False
        return True
                
                