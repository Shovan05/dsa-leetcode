class Solution:
    def asteroidCollision(self, nums: list[int]) -> list[int]:
        stack=[]
        for i in nums:
            if i>0:
                stack.append(i)
            else:
                while len(stack)!=0 and stack[-1]>0 and stack[-1]<abs(i):
                    stack.pop()
                if len(stack)!=0 and stack[-1]==abs(i):
                    stack.pop()
                elif len(stack)==0 or stack[-1]<0:
                    stack.append(i)

        return stack
        