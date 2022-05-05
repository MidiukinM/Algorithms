# input:
# 4 5 6 7 0 2 1 3
# c o d e l e e t
# output:
# 0 1 2 3 4 5 6 7
# l e e t c o d e

class Solution:
    def shuffle(self, s: str, indices: list[int]) -> str:
        new_s = [''] * len(s)

        for i, ind in enumerate(indices):
            new_s[ind] = s[i]

        return ''.join(new_s)


if __name__ == '__main__':
    s = 'codeleet'
    indices = [4, 5, 6, 7, 0, 2, 1, 3]
    print(Solution().shuffle(s, indices))