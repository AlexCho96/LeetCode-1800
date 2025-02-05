from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:        
        if len(nums) == 1:
            return nums[0]
        else:
            sum, x = [nums[0]], 0
            monotonic = True if nums[0] < nums[1] else False
            for i in range(0, len(nums)-1):
                if nums[i] < nums[i+1]:
                    sum[x] += nums[i]+nums[i+1] if not monotonic else nums[i+1]
                    monotonic = True
                else:
                    x += 1
                    monotonic = False
                    sum.append(0)

                print(sum)
            return max(sum)