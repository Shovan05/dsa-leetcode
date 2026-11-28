class Solution:
    def isPalindrome(self, s, left, right):
        # Check whether the substring is a palindrome.
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

    def backtrack(self, s, ind, temp, ans):
        # The entire string has been partitioned.
        if ind == len(s):
            ans.append(temp.copy())
            return

        for i in range(ind, len(s)):
            if self.isPalindrome(s, ind, i):

                # Choose the palindromic substring.
                temp.append(s[ind:i + 1])

                self.backtrack(s, i + 1, temp, ans)

                # Backtrack to try another substring.
                temp.pop()

    def partition(self, s):
        ans = []
        temp = []

        self.backtrack(s, 0, temp, ans)

        return ans
        