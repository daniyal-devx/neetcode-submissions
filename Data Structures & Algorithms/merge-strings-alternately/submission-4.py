class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1,n2=len(word1),len(word2)
        result=[]
        i=0
        j=0
        while i <n1 or j <n2:
            if i <n1:
                result.append(word1[i])
            if j<n2:
                result.append(word2[j])
            i+=1
            j+=1
        return "".join(result)
