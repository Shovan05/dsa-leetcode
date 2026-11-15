class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        nums=[1,2,3,4,5,6,7,8,9]
        result=[]
        self.solve(0,[],k,n,0,0,nums,result)
        return result

    def solve(self,index,subset,k,n,total,counter,nums,result):
        if total==n:
            if counter==k:
                result.append(subset.copy())
            return
        
        if total>n or counter>=k or index>=9:
            return
        
        subset.append(nums[index])
        self.solve(index+1,subset,k,n,total+nums[index],counter+1,nums,result)
        subset.pop()
        self.solve(index+1,subset,k,n,total,counter,nums,result)