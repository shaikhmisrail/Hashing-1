'''
https://leetcode.com/problems/isomorphic-strings/

Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #using Array
        sDict = [None for i in range(256)]
        tSet = [None for i in range(256)]

        for i, el in enumerate(s):
            if sDict[ord(el)] == None:
                if tSet[ord(t[i])] == None:
                    sDict[ord(el)] = t[i]
                    tSet[ord(t[i])] = ord(el)
                else:
                    
                    return False
            else:
                if sDict[ord(el)] != t[i]:
                    return False
        return True