# given the array "nums" consisting of 2n elements in the form [x1, x2, ..., xn, y1, y2, ..., yn]
# return the array in the form [x1, y1, x2, y2, ..., xn, yn]

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if len(nums) != 2 * n:
            raise ValueError('given the wrong n')
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans


if __name__ == '__main__':
    nums = [2, 5, 1, 3, 4, 5]
    n = 3
    print(Solution().shuffle(nums, n))