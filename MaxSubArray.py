from typing import List

class Solution:
    def maxSubArray(self , nums: List[int]) ->int:
        maxSub = nums[0]
        curSum = 0
       
        for n in nums:
            print("-------------------------\n")
            print("CUURENT NUMBER IS : ",n)
            if curSum < 0:
                print(curSum,"(1)")
                curSum = 0
                print(curSum , "(2)")
            curSum += n
            print(curSum , "(3)")

            maxSub = max(maxSub , curSum)
            print("max SUB array sum is :",maxSub)
        return maxSub
           
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

solution_instance = Solution()
print(solution_instance.maxSubArray(nums))