class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        nums=[1,2,3,4,5,6,7,8,9]
        result=[]
        self.backtrack(0,0,0,n,k,[],result,nums)
        return result

    def backtrack(self,index,counter,total,n,k,subset,result,nums):
        if total == n:
            if counter == k:
                result.append(subset.copy())
            return
        if total > n or counter >= k or index >= 9:
            return
        
        subset.append(nums[index])
        sum=total+nums[index]
        self.backtrack(index+1,counter+1,sum,n,k,subset,result,nums)
        sum=total
        subset.pop()
        self.backtrack(index+1,counter,sum,n,k,subset,result,nums)