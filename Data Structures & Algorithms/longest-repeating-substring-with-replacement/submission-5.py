class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        answer = 0
        freq_table = dict()

        l = 0
        r = 0
        max_freq = 0

        while r < len(s):
            r += 1
            #print("updated r to " + str(r))
            cur_char = s[r - 1]
            if cur_char in freq_table:
                freq_table.update({cur_char : freq_table.get(cur_char) + 1})
            else:
                freq_table.update({cur_char : 1})

            max_freq = max(max_freq, freq_table.get(cur_char))
            need_change = (r - l) - max_freq
            #print("updated nc to " + str(need_change))

            while need_change > k:
                l += 1
                #print("updated l to " + str(l))
                left_char = s[l - 1]
                freq_table.update({left_char : freq_table.get(left_char) - 1})
                max_freq = max(max_freq, freq_table.get(cur_char))
                need_change = (r - l) - max_freq
                #print("updated nc to " + str(need_change))

            answer = max(r - l, answer)
        
        return answer

