class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,max_r = 0,0
        j = len(heights)-1
        
        while i < j:
            #area = (j-i)*min(heights[i],heights[j])
            max_r = max(max_r, (j-i)*min(heights[i],heights[j]))
            
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max_r



        