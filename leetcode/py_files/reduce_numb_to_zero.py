# given a non-negative integer num, return the number of steps to reduce it to zero
# if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it
from math import log2


class Solution:
    def reduce_to_zero(self, num: int) -> int:
        cnt = 0
        while num != 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            cnt += 1
        return cnt

    def faster(self, num: int) -> int:
        if log2(num) - int(log2(num)) == 0:
            return log2(num) + 1
        return int(log2(num))*2


if __name__ == '__main__':
    num = 14
    print(Solution().reduce_to_zero(num))
    print(Solution().faster(num))