class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        count_s1=[0]*26
        count_window=[0]*26
        for i in range(len(s1)):
            count_s1[ord(s1[i])-ord('a')]+=1
            count_window[ord(s2[i])-ord('a')]+=1
        if count_s1==count_window:
            return True
        for r in range(len(s1),len(s2)):
            count_window[ord(s2[r])-ord('a')]+=1
            left_char=r-len(s1)
            count_window[ord(s2[left_char])-ord('a')]-=1
            if count_s1==count_window:
                return True
        return False
            
        
            
        
        