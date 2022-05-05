# input:  [5, 2, 1, 10]
# output: [2, 1, 0, 3]
# for each number in list count number of smaller numbers
from typing import List


class Solution:
    def smaller_numbers(self, nums: List[int]) -> List[int]:
        nums_sorted = sorted(nums) # O(nlogn)
        for i, el in enumerate(nums): # O(n)
            nums[i] = nums_sorted.index(el)
        return nums


if __name__ == '__main__':
    nums = [8, 1, 2, 2, 3]
    print(Solution().smaller_numbers(nums))