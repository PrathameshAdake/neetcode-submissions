class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_val, temp = 0, 0
        for i in nums:
            if i == 0: 
                temp = 0
                continue
            temp += 1
            if temp > max_val: 
                max_val = temp
        return max_val