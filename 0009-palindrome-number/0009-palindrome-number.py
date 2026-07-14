class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        rev = ""
        for i in x:
           rev = i + rev
            
        if(rev == x):
            return True
        else:
            return False