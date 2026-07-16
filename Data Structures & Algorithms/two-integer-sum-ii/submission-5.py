class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0;
        j = len(numbers)-1
        #res = []
        while i < j:
            t = numbers[i]+numbers[j]
            if target == t:
                return [i+1,j+1]
                break

            elif target > t:
                i += 1
            else:
                j -= 1
                
        #return res