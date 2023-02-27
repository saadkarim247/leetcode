class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i, n in enumerate(nums):
            if (n in hashmap):
                diff = i - hashmap[n]
                if diff <= k:
                    return True
            # print(hashmap)
            hashmap[n] = i
        return False
