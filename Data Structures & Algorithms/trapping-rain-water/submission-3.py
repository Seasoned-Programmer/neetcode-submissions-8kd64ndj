class Solution:
    def trap(self, height: List[int]) -> int:
        pre = []
        suf = []
        wt_trapped = 0
        for i in range(1,len(height)-1):
            l = max(height[0:i])
            r = max(height[i+1:len(height)])
            
            if (min(l,r)- height[i]) > 0:
                
                wt_trapped += (min(l,r)- height[i]) 
        # for i in range(len(height)-2):
        #     print(min(pre[i],suf[i])- height[i])
        #     if (min(pre[i],suf[i])- height[i]) > 0:
                
        #         wt_trapped += min(pre[i],suf[i]- height[i]) 

        return wt_trapped
        