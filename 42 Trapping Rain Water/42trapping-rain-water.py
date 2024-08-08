class Solution:
    def trap(self, arr: List[int]) -> int:
        total = 0
        maxLeft = []
        maxRight = []
        maxFromLeft, maxFromRight = 0, 0

        for index, item in enumerate(arr):
            if index == 0:
                maxLeft.append(0)
                continue
            maxFromLeft = max(maxFromLeft, arr[index - 1])
            maxLeft.append(maxFromLeft)

        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr) - 1:
                maxRight.insert(0, 0)
                continue
            maxFromRight = max(maxFromRight, arr[i + 1])
            maxRight.insert(0, maxFromRight)

        for i in range(len(arr)):
            depth = min(maxLeft[i], maxRight[i]) - arr[i]

            if depth > 0:
                total += depth

        return total