class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = []
        suffix_products = []
        ans = []
        
        prev=1
        for index, value in enumerate(nums):
            if (index == 0):
                prefix_products.append(1)
                continue
            prev = nums[index-1] * prev
            prefix_products.append(prev)

        prev = 1
        for index in range(len(nums)-1,-1,-1):
            if (index == 0):
                break
            if (index == len(nums)-1):
                suffix_products.insert(0, prev)
            
            prev = nums[index] * prev
            suffix_products.insert(0, prev)

        for i in range(len(nums)):
            ans.append(prefix_products[i]*suffix_products[i])
        print(prefix_products)
        print(suffix_products)
        return ans

        