class Solution:
    def max_positive(self,arr):
        memo = [0]*len(arr)
        memo[0] = arr[0]
        biggest = max(arr[0], 0)
        for i in range(1, len(memo)):
            memo[i] = max(arr[i], arr[i] + memo[i-1])
            biggest = max(biggest, memo[i])
        return biggest

    def max_negative(self,arr):
        memo = [0]*len(arr)
        memo[0] = arr[0]
        smallest = min(arr[0], 0)
        for i in range(1, len(memo)):
            memo[i] = min(arr[i], arr[i] + memo[i-1])
            smallest = min(smallest, memo[i])
        return smallest

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        return max(abs(self.max_negative(nums)), self.max_positive(nums))
        