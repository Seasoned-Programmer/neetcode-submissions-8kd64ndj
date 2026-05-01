class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        for i in nums:
            if i in freqDict.keys():
                freqDict[i] = freqDict[i]+1

            else:
                freqDict[i] = 1

        sorted_dict = dict(sorted(freqDict.items(), key=lambda item: item[1]))
        
        arr = list(sorted_dict.keys())
        size = len(arr)
        result = []
        while k > 0:
            result.append(arr[size-1])
            k -= 1
            size -=1

        return result
            



        

      

            





        

        

        


        
 

            
        



            

        