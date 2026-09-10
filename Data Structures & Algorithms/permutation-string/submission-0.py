class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = {}
        len1 = len(s1)
        s2_freq = {}
        len2 = 0

        for i in range(len(s1)):
            char = s1[i]

            if char in s1_freq:
                s1_freq.update({char: s1_freq.get(char) + 1})
            else:
                s1_freq.update({char: 1})

        
        l = 0

        for r in range(len(s2)):
            char = s2[r]
            len2 = r - l + 1

            if char in s2_freq:
                s2_freq.update({char: s2_freq.get(char) + 1})
            else:
                s2_freq.update({char: 1})
            
            if len2 > len1:
                l += 1
                len2 = r - l + 1

                lchar = s2[l - 1]

                if s2_freq.get(lchar) > 1:
                    s2_freq.update({lchar: s2_freq.get(lchar) - 1})
                else:
                    s2_freq.pop(lchar)

            if s2_freq == s1_freq: return True
            
        return False



