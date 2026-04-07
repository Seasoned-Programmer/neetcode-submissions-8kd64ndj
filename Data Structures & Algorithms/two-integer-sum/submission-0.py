class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetdict = {}
        for i in range(len(nums)):
            if  (target - nums[i]) in targetdict.keys():
                return [targetdict[target-nums[i]],i]
            else:
                targetdict = targetdict| {nums[i]:i} 

        

          
        