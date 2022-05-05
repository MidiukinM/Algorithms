# we are given a list nums of integers representing a list compressed with run-length encoding
# consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0)
# for each such pair, there are freq elements with value val concatenated in a sublist
# concatenate all the sublists from left to right to generate the decompressed list

# input: [1, 2, 3, 4]
# output: [2, 4, 4, 4] because 2 freqs 1 time and 4 freqs 3 times

class Solution:
    def compress_RLE_list(self, nums: list[int]) -> list[int]:
        res = []
        for i in range(0, len(nums)-1, 2):
            res += nums[i] * [nums[i+1]]
        return res


if __name__ == '__main__':
    print(Solution().compress_RLE_list([1, 2, 3, 4]))