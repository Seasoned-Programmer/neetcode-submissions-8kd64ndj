class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if self.hashstring(s) == self.hashstring(t):
            return True 
        else:
            return False

    def hashstring(self, st: str) -> dict:
        hashstr = {}
        for i in range(len(st)):
            if st[i] not in hashstr.keys():
                hashstr = hashstr | {st[i]:1}

            else:
                hashstr[st[i]] = hashstr[st[i]] + 1
        return hashstr
    