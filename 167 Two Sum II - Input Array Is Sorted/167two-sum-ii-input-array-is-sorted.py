class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i, j in enumerate(numbers):
            print(i , j)
            r = target - j
            if r in d:
                return [d[r]+1, i+1]
            else:
                d[j] = i