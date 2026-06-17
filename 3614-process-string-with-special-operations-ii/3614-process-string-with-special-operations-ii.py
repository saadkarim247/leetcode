class Solution:
    def processStr(self, s: str, k: int) -> str:
        arr = list(s)
        origlen = 0
        for i, v in enumerate(arr):
            if v == "%":
                continue
            elif v == "#":
                origlen *= 2
            elif v == "*":
                if (origlen != 0):
                    origlen -= 1
            else:
                origlen += 1
        if k >= origlen:
            return "."
        currentlen = origlen
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == "*":
                currentlen += 1
            elif arr[i] == "#":
                if k >= (currentlen // 2):
                    k = k - (currentlen // 2)
                currentlen = currentlen // 2
            elif arr[i] == "%":
                k = currentlen - k - 1
            else:
                if k == (currentlen-1):
                    return arr[i]
                currentlen -= 1
        return arr[k]
        
       
            
