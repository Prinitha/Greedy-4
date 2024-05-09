'''
TC: O(n) - iterate over the tops and bottoms not more than twice
SC: O(1) - we are dealing with only few pointers to deduce our result
'''
from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        def rotations(target):
            a_tops_rotations, a_bottoms_rotations = 0,0
            for i, v in enumerate(tops):
                if tops[i] == bottoms[i] == target:
                    continue
                if v == target:
                    a_bottoms_rotations += 1
                elif bottoms[i] == target:
                    a_tops_rotations += 1
                else:
                    return -1
            return min(a_tops_rotations, a_bottoms_rotations)
        
        a = rotations(tops[0]) 
        b = rotations(bottoms[0])
        if a == -1 and b == -1:
            return a
        if a == -1:
            return b
        elif b == -1:
            return a
        else:
            return min(a,b)
s = Solution()
print(s.minDominoRotations([2,1,2,4,2,2], [5,2,6,2,3,2]))
print(s.minDominoRotations([3,5,1,2,3], [3,6,3,3,4]))