class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        sufix = []

        def product (arr):
            res = 1
            for i in arr:
                res = res*i

            return res

        for i in range(len(nums)):
            pre = product(nums[0:i]) 
            suf = product(nums[i+1:len(nums)])

            prefix.append(pre)
            sufix.append(suf)

        
        for i in range(len(nums)):
            nums[i] = prefix[i]*sufix[i]

        return nums

        

        