'''
https://leetcode.com/problems/word-pattern/

Time Complexity: O(n)
Space Complexity: O(n)

Refer to the solution video for better impl. This one is self impl. Very edge case prone. Find/think better soln.

'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordList = s.split(" ")
        print(wordList)
        dic = {}
        uniqueWord = {}

        if len(pattern) != len(wordList):
            return False

        for i, el in enumerate(pattern):
            print(dic)
            if el not in dic and wordList[i] not in uniqueWord :
                dic[el] = wordList[i]
                uniqueWord[wordList[i]] = el
            else:
                if wordList[i] not in uniqueWord or el not in dic or dic[el] != wordList[i] or uniqueWord[wordList[i]] != el:
                    return False

        return True
