class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        para=[""]*(2*n)
        result=[]
        self.solve(0,0,para,result)
        return result

    def solve(self,index,total,para,result):
        if index == len(para):
            if total == 0:
                result.append("".join(para))
            return
        if total>len(para)//2:
            return
        if total<0:
            return    
        para[index]="("    
        sum=total+1
        self.solve(index+1,sum,para,result)
        para[index]=")"
        sum=total-1
        self.solve(index+1,sum,para,result)