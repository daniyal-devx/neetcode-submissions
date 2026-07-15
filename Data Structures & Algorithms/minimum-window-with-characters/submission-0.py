class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        need = len(count_t)  
        count_window = {}
        have = 0
        l = 0
        min_len = float('inf')
        min_l = 0

        for r in range(len(s)):
            c = s[r]
            count_window[c] = count_window.get(c, 0) + 1
            if c in count_t and count_window[c] == count_t[c]:
                have += 1
            while have == need:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    min_l = l
                left_c = s[l]
                count_window[left_c] -= 1
                if left_c in count_t and count_window[left_c] < count_t[left_c]:
                    have -= 1
                l += 1

        return "" if min_len == float('inf') else s[min_l : min_l + min_len]