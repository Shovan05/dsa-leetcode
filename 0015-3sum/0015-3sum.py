class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums=sorted(nums)
        ans=[]
        for i in range (len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue 
            right=len(nums)-1
            left=i+1
            while(left<right):
                if (nums[i]==-(nums[left]+nums[right])):
                    ans.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    right-=1
                elif (nums[i]>-(nums[left]+nums[right])):
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    right-=1
                else:
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    left+=1
        return ans
                    
