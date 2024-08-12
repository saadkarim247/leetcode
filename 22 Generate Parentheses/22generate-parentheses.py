class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(openCount, closeCount, path):
            if openCount == closeCount == n:
                ans.append(path)

            if openCount < n:
                backtrack(openCount + 1, closeCount, path + "(")

            if closeCount < openCount:
                backtrack(openCount, closeCount + 1, path + ')')
            

        backtrack(0, 0, "")
        return ans
        