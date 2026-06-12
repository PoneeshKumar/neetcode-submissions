class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # length of last word, start at the end of string and move
        # backwards, add counter return counter
        i = len(s) - 1

        # skip trailing spaces
        while i >= 0 and s[i] == " ":
            i -= 1

        counter = 0

        # count last word
        while i >= 0 and s[i] != " ":
            counter += 1
            i -= 1

        return counter
        