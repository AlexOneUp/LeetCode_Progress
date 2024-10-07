class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = [0,1]
        
        l = 0
        r = len(numbers) - 1
        
        while (l < r) :
            if target - numbers[r] == numbers[l]:
                res[0] = l + 1
                res[1] = r + 1
                return res
            if (numbers[l] + numbers[r]) < target :
                l+=1
            else:
                r-=1
        return res
#Approach :
#_____________________________________________________________
#2 ptr approach instead of a O(n^2) loop. compare the (target - i) is a valid j value in nums[]. return indexes in array of sz 2. in case the sum of 2 nums is LESS than the target iterate i, otherwise decrement j

# //EDGECASE : The tests are generated such that there is exactly one solution