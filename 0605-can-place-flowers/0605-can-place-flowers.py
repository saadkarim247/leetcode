class Solution:
    def firstElement(self, index: int) -> bool:
        return index==0
    def lastElement(self, index:int , length:int) -> bool:
        return index==length-1
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if (n==0):
            return True
        if (len(flowerbed))==1:
            return True if n<=1 and flowerbed[0]==0 else False
        else:
            for index,value in enumerate(flowerbed):
                if self.firstElement(index) and value==0:
                    if (flowerbed[index+1] is not 1):
                        flowerbed[index] = 1
                        n-=1
                elif self.lastElement(index, len(flowerbed)):
                    if (value==0):
                        if (flowerbed[index-1] is not 1):
                            flowerbed[index] = 1
                            n-=1
                            break
                    else:
                        break
                else:
                    if (flowerbed[index-1] is not 1 and flowerbed[index+1] is not 1 and value == 0):
                        flowerbed[index] = 1
                        n-=1
                    else:
                        continue
                if n == 0:
                    return True
            return n==0
