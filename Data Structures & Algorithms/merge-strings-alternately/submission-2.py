class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result =[]
        for c1,c2 in zip_longest(word1,word2,fillvalue=""):
            result.append(c1)
            result.append(c2)
        return "".join(result)
