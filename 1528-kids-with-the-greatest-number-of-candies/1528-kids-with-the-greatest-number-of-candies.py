class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = 0
        ans = []
        for candy in candies:
            greatest = max(candy,greatest)

        for candy in candies:
            if (candy+extraCandies >= greatest):
                ans.append(True)
            else:
                ans.append(False)

        return ans