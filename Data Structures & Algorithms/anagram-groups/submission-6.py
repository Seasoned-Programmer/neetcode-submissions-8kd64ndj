class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # a static alphabet dictionary with default values as 0 
        alphabetDict = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        # empty dictionary to store anagrams
        anagramGroups = {}

        #iteration logic
        for i in strs:
            #iterating through characters of strings and counting to update alphabet dictionary 
            for j in i:
                alphabetDict[j] = alphabetDict[j]+ 1
            
            #recovering the str to update as key in anagrams dictionary
            strKey = ''
            for key in alphabetDict.keys():
                if alphabetDict[key] > 0:
                    strKey = strKey + key*alphabetDict[key]
            
            # adding/updating values in anagram dictionary 
            if strKey not in anagramGroups.keys():
                anagramGroups[strKey] = [i]
            else:
                anagramGroups[strKey] = anagramGroups[strKey] + [i]  

            #reseting alphabet dictionary for next cycle
            alphabetDict = {key: 0 for key in alphabetDict}

            #end of for loop

        #generating results to return
        result = []
        for i in anagramGroups.values():
            result.append(i)
            
        return result



        