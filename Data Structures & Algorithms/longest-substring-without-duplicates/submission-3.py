class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        has = []
        has_s = len(has)
        for r in range(len(s)):
            if s[r] not in has:
                has.append(s[r])
            else:
                while s[r] in has:
                    l += 1
                    del has[0]
                has.append(s[r])
            
            has_s = max(r-l+1,has_s)
            

        return has_s





        