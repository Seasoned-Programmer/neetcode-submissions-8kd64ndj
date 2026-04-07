class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        results = {}
        for i in nums:
            if i not in results.keys():
                results = results | {i:1}

            else:
                return True

        return False

        