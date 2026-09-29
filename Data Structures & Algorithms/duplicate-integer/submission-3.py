class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_dictionary = {}
        for num in nums:
            if num in duplicate_dictionary:
                duplicate_dictionary[num] += 1
                return True
            else:
                duplicate_dictionary[num] = 1
        return False
        
        

        