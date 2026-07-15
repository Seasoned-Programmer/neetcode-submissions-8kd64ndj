class Solution:

    def encode(self, strs: List[str]) -> str:
        encodeStr = ""
        for i in strs:
            encodeStr = encodeStr+str(len(i))+"#"+i

        return encodeStr
            
    def decode(self, s: str) -> List[str]:
        k = 0
        i = 0
        decodeList = []
        while i < len(s):
            if s[i] == "#":
                
                decodeList.append(s[i+1:i+1+int(s[k:i])])
                i = i+1+int(s[k:i])
                k = i
               
            else:
                i +=1

        return decodeList        





