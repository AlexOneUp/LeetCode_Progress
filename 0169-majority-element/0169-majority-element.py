class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = 0
        

        for i in nums:
            if count == 0: res = i
            if i == res: count += 1
            else : count -= 1
        return res


#class Solution(object):
    # def majorityElement(self, nums):
    #     sol = None
    #     cnt = 0
    #     for i in nums:
    #         if cnt == 0:
    #             sol = i
    #         cnt += (1 if i == sol else -1)
    #     return sol