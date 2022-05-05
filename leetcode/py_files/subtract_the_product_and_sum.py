# given an int number n, return the diff between the product of its digits and the sum of its digits

class Solution:
    def subtract_product_and_sum(self, n: int) -> int:
        prod = 1
        summa = 0
        while n % 10 != 0:
            prod *= n % 10
            summa += n % 10
            n //= 10
        return prod - summa


if __name__ == '__main__':
    print(Solution().subtract_product_and_sum(4421))