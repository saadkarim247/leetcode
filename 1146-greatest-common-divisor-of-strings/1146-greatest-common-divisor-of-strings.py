class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        a = str1
        b = str2
        if (len(str1) == len(str2)):
            while(len(a) is not 0):
                check = b.replace(a, "")
                if (len(check) == 0):
                    return a
                else:
                    a = a[:-1]
            return ""

        else:
            small = str1 if len(str1) < len(str2) else str2
            large = str1 if len(str1) > len(str2) else str2
            small2 = small
            large2 = large
            while(len(small) is not 0):
                check = large.replace(small, "")
                if (len(check) == 0):
                    if (len(small2.replace(small,"")) is 0):
                        return small
                    else: 
                        small = small[:-1]
                else:
                    small = small[:-1]
            return ""
       