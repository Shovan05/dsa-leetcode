class Solution:
    def totalFruit(self, nums: list[int]) -> int:
        maxi=0
        left=0
        right=0 
        n=len(nums)
        seen={}
        while right<n:
            seen[nums[right]] = seen.get(nums[right], 0) + 1
            if len(seen)>2:
                seen[nums[left]] -= 1
                if seen[nums[left]]==0:
                    del seen[nums[left]]
                left+=1
            if len(seen)<=2 :
                maxi=max(maxi,right-left+1)
            right+=1
        return maxi
        

        