class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for i in range(len(strs)):
            
            sortedStrs = "".join(sorted(strs[i]))
            if sortedStrs not in anagram.keys():
                anagram = anagram|{sortedStrs:[(strs[i])]}

            else:
                anagram[sortedStrs] = anagram[sortedStrs] + [(strs[i])]

        anagramGroups = []
        for items in anagram.values():
            anagramGroups.append(items)
    
        return anagramGroups
        