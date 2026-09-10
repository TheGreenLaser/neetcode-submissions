class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) ==1: return len(s)
        d = dict()
        ret = 0
        p1 = 0
        p2 = 0

        while p2 < len(s):
            p2 += 1
            c = s[p2-1:p2]

            if c in d:
                p1 = max(d.get(c) + 1, p1)

            d.update({c : p2-1})
            ret = max(ret, (p2 - p1))
    

        return ret



            