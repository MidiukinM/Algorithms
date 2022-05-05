# class for sparse vector
class SparseVector:
    def __init__(self, nums):
        self.length = len(nums)
        self.sparse_dict = {}
        for i, el in enumerate(nums):
            if el:  # если элемент не 0
                self.sparse_dict[i] = el

    def dot_product(self, vec):
        if self.length != vec.length:
            raise ValueError('Vectors should have equal length')
        else:
            d1 = self.sparse_dict
            d2 = vec.sparse_dict
            dp = 0
            for key in (d1.keys() & d2.keys()):
                dp += d1[key] * d2[key]
            return dp


if __name__ == '__main__':
    nums1 = [1, 2, 0, 0, 10]
    nums2 = [0, 1, 0, 4, 2]
    sv1 = SparseVector(nums1)
    sv2 = SparseVector(nums2)
    print(sv1.dot_product(sv2))
