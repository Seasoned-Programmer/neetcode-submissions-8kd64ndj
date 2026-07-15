class Solution:

    def encode(self, strs: List[str]) -> str:
        encodeStr = ""
        for i in strs:
            encodeStr = encodeStr+str(len(i))+"#"+i

        return encodeStr
            
    def decode(self, s: str) -> List[str]:
        k = 0
        decodeList = []
        i = 0
        while i < len(s):
            
            if s[i] == "#":
                #print(k == i-1)
                st = s[k:i]
                size = int(st)
                
                str1 = s[i+1:i+1+size]
                decodeList.append(str1)
                i = i+1+size
                
                k = i
               
            else:
                i +=1    
        return decodeList        





