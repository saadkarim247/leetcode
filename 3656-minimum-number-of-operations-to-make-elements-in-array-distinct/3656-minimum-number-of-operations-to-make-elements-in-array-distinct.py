class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        track = set()
        n = len(nums)
        for i in range(n-1, -1, -1):
            if nums[i] in track:
                return (i//3)+1
            track.add(nums[i])
        return 0
        