from typing import List


class Solution:
    def running_sum(self, nums: List[int]) -> List[int]:
        ans = []
        cur_sum = 0
        for el in nums:
            cur_sum += el
            ans.append(cur_sum)
        return ans


if __name__ == '__main__':
    print(Solution().running_sum([1, 2, 5]))
