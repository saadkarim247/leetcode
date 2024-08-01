class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanString = ''.join(char for char in s if char.isalnum()).lower()
        r = len(cleanString) - 1
        mid = (len(cleanString)//2) 
        for i in range (mid):
            if (cleanString[i] == cleanString[r]):
                r-=1
            else: 
                return False
        return True