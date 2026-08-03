class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        seen={}
        for i in strs:
            key=''.join(sorted(i))
            if key not in seen:
                seen[key] = [i]
            else:
                seen[key].append(i) 
        return list(seen.values())     