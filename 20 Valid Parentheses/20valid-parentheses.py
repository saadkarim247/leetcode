class Solution:
    def isValid(self, s: str) -> bool:
        store = {
            '}': '{',
            ']': '[',
            ')' : '('
        }
        stack = []
        for c in s:
            if (c in store.values()):
                stack.append(c)
            if (c in store):
                if (len(stack) == 0 or stack.pop() != store[c]):
                    return False

        if (len(stack) == 0):
            return True
        return False