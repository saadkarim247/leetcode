class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return 0
        # for i in range(0,len(nums)):
        #     if (i == 0):
        #         if (self.findSumOfArray(nums[1:len(nums)]) == 0):
        #             return i
        #     elif i == len(nums)-1:
        #         if (self.findSumOfArray(nums[0:i]) == 0):
        #             return i
        #     else:
        #         if (self.findSumOfArray(nums[0:i]) == self.findSumOfArray(nums[i+1:len(nums)])):
        #             return i
        # return -1
        pivot = 0 
        total = sum(nums)
        left = 0 
        while pivot < len(nums):
            right = total - nums[pivot] - left
            if (right == left):
                return pivot
            left += nums[pivot]
            pivot+=1
        return -1

                


    # def findSumOfArray(self, arr: List[int]) -> int:
    #     sum = 0
    #     for i in range(0,len(arr)):
    #         sum+=arr[i]
    #     return sum