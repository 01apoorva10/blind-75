class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        print("Starting function execution.")
        
        # Check if the length of the set of nums is not equal to the length of nums
        if len(set(nums)) != len(nums):
            print("Duplicate found! Returning True.")
            return True
        else:
            print("No duplicates found. Returning False.")
            return False

# usage
sol = Solution()
nums = [1, 2, 3, 4, 5]
print("Calling containsDuplicate with nums:", nums)
print("Result:", sol.containsDuplicate(nums))
