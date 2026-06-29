class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = list(s)
        left = 0
        right = 0
        maxLen = 0
        hashset = set()
        while right < len(arr):
            if arr[right] in hashset:
                while(arr[right] in hashset):
                    hashset.remove(arr[left])  
                    left += 1
            hashset.add(arr[right])
                # maxLen = max(maxLen, currentLen)
            print(hashset)
            print(left,right)
            maxLen = max(maxLen, right - left + 1)
            right += 1

            # print(right - left + 1, maxLen)
        return maxLen
