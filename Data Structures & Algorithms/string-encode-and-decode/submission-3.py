class Solution:

    def encode(self, strs: List[str]) -> str:
        encodeStr = ""
        for i in strs:
            encodeStr = encodeStr+str(len(i))+"ā"+i

        return encodeStr
            
            
        

    def decode(self, s: str) -> List[str]:

        k = 0
        decodeList = []
        for i in range(len(s)):
            if s[i] == "ā":
                
                if k == i-1:
                    size = int(s[k])
                
                size = int(s[k:i])
                
                str1 = s[i+1:i+1+size]
                decodeList.append(str1)
                i = i+1+size
                k = i
                
        return decodeList
