class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        else:
            seen={}
            for i in s:
                if i in seen:
                    seen[i]+=1
                else:
                    seen[i]=1
            for i in t:
                if i in seen:
                    seen[i]-=1
            for i in seen:
                if seen[i]!=0:
                    return False
            return True