class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s)-1
        liststr = list(s)
        vowels = {'a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        while (left < right):
            if (liststr[left] in vowels):
                if (liststr[right] in vowels):
                    liststr[left],liststr[right] = liststr[right], liststr[left]
                    left +=1
                    right -=1
                else :
                    right-=1
            else:
                left+=1
        return "".join(liststr)

            
