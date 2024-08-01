class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)

        maxCount = 0
        for item in nums:
            if (item-1 not in store):
                count = 0
                while ((item+count) in store):
                    count+=1
                maxCount = max(count, maxCount)
        
        return maxCount