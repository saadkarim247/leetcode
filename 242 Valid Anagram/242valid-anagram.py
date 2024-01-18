class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       if (len(s) != len(t)):
           return False
       
       for char in s:
            if char not in t:
                return False
            s = s.replace(char,'', 1)
            t = t.replace(char,'',1)
            if(len(s) == 0):
                return True
       