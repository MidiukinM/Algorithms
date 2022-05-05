# given 2 arrays nums1 and nums2 of length n
# return the minimum product sum if you are allowed to rearrange the order of the elements in nums1
from typing import List


class Solution:
    def min_product_sum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort(reverse=True)
        return sum(i*j for i, j in zip(nums1, nums2))


if __name__ == '__main__':
    nums1 = [5, 3, 4, 2]
    nums2 = [4, 2, 2, 5]
    print(Solution().min_product_sum(nums1, nums2))

