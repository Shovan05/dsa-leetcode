class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}
        arr=[]
        for i in range(len(nums)):
            if (target-nums[i]) in seen:
                arr.append(seen[target-nums[i]])
                arr.append(i)
                break
            else:
                seen[nums[i]]=i
        return arr