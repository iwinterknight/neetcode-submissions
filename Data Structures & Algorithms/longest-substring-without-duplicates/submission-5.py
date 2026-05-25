class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        l = 0
        max_len = 0
        for i, c in enumerate(s):
            if c in st:
                while c in st:
                    pop_c = s[l]
                    st.remove(pop_c)
                    l += 1
            st.add(c)
            max_len = max(max_len, i-l+1)            
        return max_len 
