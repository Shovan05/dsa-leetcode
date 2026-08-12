class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # k >= window_length - max_freq
        ''' seen={}
        left=0
        right=0
        max_freq=0
        max_length=0

        for letter in s:
            if letter not in seen:
                seen[letter]=1
                right+=1
                max_freq=max(max_freq,seen[letter])
            else:
                seen[letter]+=1
                right+=1
                max_freq=max(max_freq,seen[letter])
                
            while (right-left-1)-max_freq<=k:
                max_length=max(max_length,(right-left-1))
                continue
            
            seen[s[left]]-=1
            left+=1
        
        return(max_length)'''
        seen = {}
        left = 0
        max_freq = 0
        max_length = 0

        for right in range(len(s)):
            letter = s[right]
            seen[letter] = seen.get(letter, 0) + 1
            max_freq = max(max_freq, seen[letter])
            
            while (right - left + 1) - max_freq > k:
                # shrink: what needs to happen to `seen` and `left` here?
                seen[s[left]]-=1
                left+=1
                
            
            max_length = max(max_length, right - left + 1)

        return max_length



