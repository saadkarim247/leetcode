class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        steps = min(len(word1), len(word2))
        ans = ""
        for i in range(0, steps):
            if (len(word1) == len(word2)):
                ans = ans + word1[i] + word2[i]
            elif (len(word1) < len(word2)):
                if (i < len(word1)-1):
                    ans = ans + word1[i] + word2[i]
                else:
                    ans = ans + word1[i] + word2[i:]
                    break
            else:
                if (i < len(word2)-1):
                    ans = ans + word1[i] + word2[i]
                else:
                    ans = ans + word1[i] + word2[i] + word1[i+1:]
                    break
        return ans
