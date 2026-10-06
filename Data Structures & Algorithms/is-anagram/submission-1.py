class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        dictionary = {}

        for i in range(len(s)):
            dictionary[s[i]] = 1 + dictionary.get(s[i],0)
            dictionary[t[i]] = dictionary.get(t[i],0) - 1

        for x in dictionary:
            if dictionary[x] != 0:
                return False
        
        return True
        