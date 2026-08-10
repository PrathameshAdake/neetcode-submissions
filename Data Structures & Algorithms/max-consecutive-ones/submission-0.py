class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sizee, maxx = len(nums), 0

        for i in range(sizee):
            temp = 0
            for j in range(i, sizee):
                if nums[j] == 0: break
                temp += 1
            maxx = max(temp,maxx)

        return maxx