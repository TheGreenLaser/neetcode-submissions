class Solution:
    def isPalindrome(self, s: str) -> bool:
        #try two pointers
        pointer1 = 0
        pointer2 = len(s) - 1

        while(pointer1 < pointer2):
            s1 = s[pointer1].lower()
            s2 = s[pointer2].lower()

            while(not s1.isalpha() and not s1.isdigit()):
                pointer1 += 1
                if(pointer1 > pointer2):
                    break
                s1 = s[pointer1].lower()

            while(not s2.isalpha() and not s2.isdigit()):
                pointer2 -= 1
                if(pointer1 > pointer2):
                    break
                s2 = s[pointer2].lower()

            if(pointer1 > pointer2):
                break

            if(s1 != s2):
                return False

            pointer1 += 1
            pointer2 -= 1

        return True
