class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_p = 0
        right_p = len(s) - 1
        
        while left_p < right_p:
            if not s[left_p].isalnum():
                left_p += 1
            elif not s[right_p].isalnum():
                right_p -= 1
            elif s[left_p].lower() != s[right_p].lower():
                return False
            else:
                left_p += 1
                right_p -= 1

        return True


     

        

        

