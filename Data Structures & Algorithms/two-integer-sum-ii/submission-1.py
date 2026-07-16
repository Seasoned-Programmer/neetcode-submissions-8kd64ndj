class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0;
        j = len(numbers)-1
        res = []
        while i < len(numbers):
            if target == numbers[i]+numbers[j]:
                res = [i+1,j+1]
                break

            elif target > numbers[i]+numbers[j]:
                i = i+1
            else:
                j = j-1
                
        return res