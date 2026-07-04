class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newstr=""
        i=0
        j=0
        n1=len(word1)
        n2=len(word2)
        while i <n1 or j <n2:
            if i <n1:
                newstr+=word1[i]
            if j<n2:
                newstr+=word2[j]
            i+=1
            j+=1
        return newstr
