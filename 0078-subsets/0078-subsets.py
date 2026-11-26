class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result=[]
        self.solve(0,[],nums,result)
        return result

    def solve(self,index, subset,nums,result):
        if index>=len(nums) :
            result.append(subset.copy())
            return
        subset.append(nums[index])
        self.solve(index+1,subset,nums,result)
        subset.pop()
        self.solve(index+1,subset,nums,result)