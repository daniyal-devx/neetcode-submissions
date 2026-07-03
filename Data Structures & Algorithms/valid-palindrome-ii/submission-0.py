class Solution:
    def validPalindrome(self, s: str) -> bool:
        n=len(s)
        for i in range(n):
            newstring=""
            for j in range(n):
                if j==i:
                    continue
                newstring+=s[j]
            if self.ispalindrome(newstring):
                return True
        return False
    def ispalindrome(self,s):
        return s==s[::-1]
            
       
            
        