class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ans=False
        seen=set()
        for i in range (len(nums)):
            if nums[i] in seen:
                ans=True
                break
            else:
                seen.add(nums[i])
        return ans

        