class Solution:
    def remove_vowels(self, s: str) -> str:
        vowels = ('a', 'e', 'i', 'o', 'u')
        return ''.join([l for l in s if l not in vowels])


if __name__ == '__main__':
    s = Solution()
    print(s.remove_vowels('aeiouf'))