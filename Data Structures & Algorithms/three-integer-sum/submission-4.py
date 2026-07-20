class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):

            j = i+1
            k = len(nums)-1

            while j < k:
                sum1 = nums[i] + nums[j] + nums[k]
                
                if sum1 == 0:
                    res1 = sorted(([nums[i],nums[j],nums[k]]))
                    if res1 not in res:
                        res.append(res1)
                    j +=1
                    k -=1
                elif sum1 < 0:
                    j += 1
                else:
                    k -= 1

        return res
        