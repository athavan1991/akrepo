from collections import defaultdict

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dicta = {}
        
        for idx, num in enumerate(nums):
            dicta[num] = idx;
        
        for idx, num in enumerate(nums):
            expected = target - num
            a = dicta.get(expected)
            if a != None and idx != a:
                return [idx, a]
        
        return None

# to store duplicate entries in dictinary in python
# create a defaultdict of list
# then append to that particular using key

#corner case
#[3,3] 6