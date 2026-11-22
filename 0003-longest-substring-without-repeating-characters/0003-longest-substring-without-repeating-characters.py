class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        window={}
        max_length=0
        right=0
        while right<len(s):
            if s[right] in window:
                left= max(left,window[s[right]]+1)
            window[s[right]]=right
            max_length=max(max_length,(right-left+1))
            right+=1
        
        return max_length

        