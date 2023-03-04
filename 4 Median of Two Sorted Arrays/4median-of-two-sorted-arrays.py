import math


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1 + nums2)

        if (len(nums3)%2 != 0):
            return(nums3[int((len(nums3)-1)/2)])
        else:
            x = math.floor((len(nums3)-1)/2)
            y = math.ceil((len(nums3)-1)/2)
            # print(x,y)
            return((nums3[x]+nums3[y])/2)