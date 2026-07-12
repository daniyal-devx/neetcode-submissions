class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        window={}
        maxf=0
        l=0
        for r in range(len(s)):
            window[s[r]]=window.get(s[r],0)+1
            maxf=max(maxf,window[s[r]])
            if (r-l+1)-maxf>k:
                window[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
        
        