class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # d = {}
        # for i in strs:
        #     key = tuple(sorted(i))
        #     d[key] = d.get(key, []) + [i]
        #     # print("key", key)
        #     # print('value',d.get(key, []))
        # return d.values()
        
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')]+=1
            res[tuple(count)].append(s)

        return res.values()
