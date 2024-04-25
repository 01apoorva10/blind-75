class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen_elements = {}
        
        print(seen_elements)
        for i, a_num in enumerate(nums):
            print(i,a_num)
            print(" \n ----seen_elements : ",seen_elements)
            complement = target - a_num
            print("complement ", complement)
            if complement in seen_elements:   
                print("seen_elements[complement]:",seen_elements[complement] , i )
                print( "seen_elements  : " , seen_elements )
                return [seen_elements[complement], i]
            seen_elements[a_num] = i
            print("seen_elements[a_num] : " , seen_elements[a_num]  , " a_num  : is  :" , a_num )
        # return []

# Provide custom values for nums and target
custom_nums = [2, 7, 11, 15]
custom_target = 9

# Create an instance of the Solution class
solution = Solution()

# Call the twoSum method with custom values
result = solution.twoSum(custom_nums, custom_target)

print("Custom nums:", custom_nums)
print("Custom target:", custom_target)
print("Result indices:", result)