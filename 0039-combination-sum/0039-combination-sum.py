class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result=[]
        self.solve(0,0,[],target,candidates,result)
        return result

    def solve(self,index,total,subset,target,candidates,result):
        if total==target: 
            result.append(subset.copy())
            return
        elif total>target:
            return
        if index>=len(candidates):
            return
        subset.append(candidates[index])
        sum=total+candidates[index]
        self.solve(index,sum,subset,target,candidates,result)
        e=subset.pop()
        sum=sum-e
        self.solve(index+1,sum,subset,target,candidates,result)