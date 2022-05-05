# you have n boxes. you are given a binary string boxes of length n
# where boxes[i] is 0 if the 1th box is empty and 1 if it contains one ball
# we can move one ball from a box to an adjacent (neighbour) box.
# return an array answer of size n,
# where answer[i] is the min number of operations needed to move all the balls to the i-th box
from typing import List


class Solution:
    def all_balls(self, boxes: str) -> List[int]:
        leftones, leftcost, rightones, rightcost, n = 0, 0, 0, 0, len(boxes)
        ans = [0] * n
        for i in range(1, n):
            if boxes[i-1] == '1':
                leftones += 1
            leftcost += leftones
            ans[i] = leftcost
        for i in range(n-2, -1, -1):
            if boxes[i+1] == '1':
                rightones += 1
            rightcost += rightones
            ans[i] += rightcost
        return ans


if __name__ == '__main__':
    print(Solution().all_balls('1101'))


