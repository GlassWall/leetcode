from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_l = 0
        lookup = {}
        cum_sum = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cum_sum += 1
            elif nums[i] == 0:
                cum_sum -= 1

            if cum_sum == 0:
                max_l = i + 1
            elif cum_sum in lookup:
                max_l = max(max_l, i - lookup[cum_sum])
            else:
                lookup[cum_sum] = i
        return max_l

if __name__ == "__main__":
    nums = [1, 0, 0 , 1, 0, 1]
    obj = Solution()
    print(obj.findMaxLength(nums=nums))