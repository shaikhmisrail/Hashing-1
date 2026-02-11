'''
https://leetcode.com/problems/group-anagrams/description/
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Time Complexity: O(n)
Space Complexity: O(n)
'''

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashset = defaultdict(list)

        for el in strs:
            hash1 = self.getHash(el)
            hashset[hash1].append( el)
        return [v for v in hashset.values()]
    
    def getHash(self, word):
        prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
        hash1 = 1
        for c in word:
            hash1 = hash1 * prime[ord(c) -ord('a')]
        return hash1