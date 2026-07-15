class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = "".join( i.upper() for i in s if i.isalnum())
        if s == "" or len(s) == 1:
            return True
        #print(s)
        i = 0 
        j = len(s)-1
        res = True
        
        while i < ((len(s)/2)+1):
            #print(i,j)
            if s[i] != s[j]:
                res = False
                break        
            i +=1
            j -=1

        return res


        

        