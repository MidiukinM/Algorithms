# there is a hidden integer array arr that consists of n non-neg integers
# it was encoded into another integer array encoded of length n-1, such that:
# encoded[i] = arr[i] XOR arr[i+1]
# example: arr = [1, 0, 2, 1], then encoded = [1, 2, 3]
# you are given encoded array and first integer of arr = arr[0]. Return the original arr
# xor = (a and not b) or (not a and b)
# xor of integers is: 6 xor 3 is 5 because 110 and 011 -> 101 (binary operations)
# (6 xor 3 = 5)  and (5 xor 3 = 6) and (5 xor 6 = 3)

class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        n = len(encoded)
        arr = [0] * (n+1)
        arr[0] = first
        for i in range(n):
            arr[i+1] = encoded[i] ^ arr[i]
        return arr
    

if __name__ == '__main__':
    print(Solution().decode([1, 2, 3], 1))