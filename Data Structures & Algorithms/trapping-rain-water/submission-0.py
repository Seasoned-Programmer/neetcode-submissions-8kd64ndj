class Solution:
    def trap(self, height: List[int]) -> int:
        i = 1
        wt_trap = 0
        for i in range(1,len(height)-1):
            #print(i)
            #l = i-1
            #r = i+1
            l = max(height[0:i])
            r = max(height[i+1 : len(height)])
            wt_pos = min(l,r) - height[i]
            print("wt_pos",wt_pos)
            if wt_pos > 0:
                wt_trap = wt_trap + wt_pos
            print("wt_trap",wt_trap)

        print(wt_trap)
        return wt_trap


        
        