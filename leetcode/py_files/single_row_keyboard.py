# there is a special keyboard with all keys in a single row
# given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25)
# initially, your finger is at index 0.
# To type a character, you have to move your finger to the index of the desired character
# The time taken to move your finger from index i to index j is |i - j|
# you want to type a string "word". Write a function to calculate how much time it takes to type it with one finger
# input: keyboard = 'abcdefghijklmnopqrstuvwxyz', word = 'cba'
# output: total time = 2 + 1 + 1 = 4

class Solution:
    def calculate_time(self, keyboard: str, word: str) -> int:
        d = {}
        for i, s in enumerate(keyboard):
            d[s] = i

        time = 0
        finger = 0
        for letter in word:
            time += abs(d[letter] - finger)
            finger = d[letter]
        return time


if __name__ == '__main__':
    print(Solution().calculate_time(keyboard='pqrstuvwxyzabcdefghijklmno', word='leetcode'))
