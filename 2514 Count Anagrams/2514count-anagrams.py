class Solution:
    # def factorial(self, n):
    #     if n == 1:
    #         return 1
    #     x = n
    #     for i in range(n, 1, -1):
    #         x *= i - 1
    #     return x

    def countAnagramsOfString(self, string: str):
        numerator = math.factorial(len(string))
        characters = tuple(sorted(string))
        count = {}
        for char in characters:
            fetchedCount = count.get(char, 0)
            updatedCount = fetchedCount + 1
            count[char] = updatedCount

        ls = count.values()
        denominator = 1
        for number in ls:
            denominator *= math.factorial(number)

        return int(numerator // denominator)

    def countAnagrams(self, s: str) -> int:
        allStrings = s.split()
        answer = 1
        for string in allStrings:
            answer *= self.countAnagramsOfString(string)
        return answer % (10**9 + 7)
