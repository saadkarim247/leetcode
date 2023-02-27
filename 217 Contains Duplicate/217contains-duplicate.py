from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        flag = True
        for i in range(len(nums)):
            if (counter[nums[i]] > 1):
                flag = False
                return True
                break
            
        if (flag):
            return False