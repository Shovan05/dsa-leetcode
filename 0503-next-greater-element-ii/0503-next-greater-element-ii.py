class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        stack=[]
        ans=[-1]*n
        for i in range (2*n-1,-1,-1):
            while (len(stack)!=0 and stack[-1]<=nums[i%n]):
                stack.pop()
            if len(stack)!=0 and i<n:
                ans[i]=stack[-1]
            stack.append(nums[i%n])
        return ans
        