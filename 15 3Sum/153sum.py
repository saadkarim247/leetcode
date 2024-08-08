class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # store = {}
        # ans = set()

        # for index,item in enumerate(nums):
        #     store[item] = index

        # for index,item in enumerate(nums):
        #     target = 0 - item

        #     for i,val in enumerate(nums):
        #         if index != i:
        #             target2 = target - val
        #             if (target2 in store):
        #                 if store[target2] != index and store[target2] != i:
        #                     # print(index, i, store[target2])
        #                     ans.add(tuple(sorted([item, val, target2])))
        #             else:
        #                 continue
        #         else:
        #             continue

        # unique_ans = [list(t) for t in ans]
        # return unique_ans
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate elements
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # Skip duplicate elements
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # Skip duplicate elements
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result