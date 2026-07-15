class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        hash_ = []
        for i in range(len(nums)):
            if (nums[i]-1) not in num_set:
                hash_.append(nums[i])
                

        #print(hash_)
        hash_ = set(hash_)
        print(hash_)
        lcs1 = 0
        #lcs = 1
        for i in hash_:
            lcs = 1
            while i+1 in nums:
                print(i+1)
                lcs = lcs+1
                i = i+1
                print(i+1)
                print(10 in nums)


            if lcs > lcs1:
                lcs1 = lcs
        #print(lcs1)
        return lcs1

        


