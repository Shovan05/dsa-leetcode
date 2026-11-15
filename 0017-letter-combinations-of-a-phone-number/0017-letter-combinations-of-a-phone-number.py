class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result=[]
        self.solve(0,[],phone_map,digits,result)
        return result

    def solve(self,index,subset,phone_map,digits,result):
        if index>=len(digits):
            result.append("".join(subset))
            return

        for i in phone_map[digits[index]]:
            subset.append(i)
            self.solve(index+1,subset,phone_map,digits,result)
            subset.pop()
 