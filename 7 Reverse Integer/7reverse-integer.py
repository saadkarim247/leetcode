class Solution:
    def reverse(self, x: int) -> int:
        ans = ""
        isNegative = False
        if x<0:
            isNegative = True
            
        string = str(x)
        # print(string)
        if (isNegative):
            string = string[1:]
        
        for i in range(len(string)-1,-1,-1):
            ans = ans + string[i]
        
        if(isNegative):
            ans = "-" + ans

        if (int(ans) > (2**31)-1) or (int(ans)<(-2**31)):
            return 0
        else: 
            return int(ans)