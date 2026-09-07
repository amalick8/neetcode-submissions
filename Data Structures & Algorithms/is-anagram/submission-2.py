class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_1 = {}
        dict_2 = {}
        for letter in s:
            if letter not in dict_1:
                dict_1[letter] = 1
            else:
                dict_1[letter] += 1
        for letter in t:
            if letter not in dict_2:
                dict_2[letter] = 1
            else:
                dict_2[letter] += 1
        
        if dict_1 == dict_2:
            return True
        else: 
            return False
        return False
        
        

        