class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ins = 1
        count = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                count += 1
                nums[ins] = nums[i+1]
                ins += 1
        return count
        