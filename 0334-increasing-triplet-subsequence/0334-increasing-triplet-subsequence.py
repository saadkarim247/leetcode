import sys

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstSmallest = float('inf')
        secondSmallest = float('inf')
        
        for num in nums:
            if num <= firstSmallest:
                firstSmallest = num
            elif num <= secondSmallest:
                secondSmallest = num
            else:
                return True
        return False
            
