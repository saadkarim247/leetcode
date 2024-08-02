class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        prevValue = 0
        for item in reversed(s):
            value = mapping[item]
            if (value < prevValue):
                total -= value
            else:
                total += value
            prevValue = value
        return total
