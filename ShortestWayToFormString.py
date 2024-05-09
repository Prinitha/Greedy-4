'''
TC O(S+TlogS) - going through S initially to create the map
                iterating over T and finding the next immediate index using 
                    Binary Search
SC O(S) - for creating the dictionay but we will have only 26 characters.
            Hence we can take it to be O(1)
'''
import collections

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        hmap = collections.defaultdict(list)
        for i, v in enumerate(source):
            hmap[v].append(i)
        
        count = 1
        prevIndex = -1  # Previous index found in source string
        
        def binarySearch(arr, target):
            left, right = 0, len(arr) - 1
            result = len(arr)
            while left <= right:
                mid = (left+right) // 2
                if arr[mid] >= target:
                    result = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return result
        
        for v in target:
            if v not in hmap:
                return -1
            
            indices = hmap[v]
            index = binarySearch(indices, prevIndex + 1)  # Find the index greater than prevIndex
            if index == len(indices):  # If no index found, reset prevIndex and increment count
                count += 1
                prevIndex = indices[0]
            else:
                prevIndex = indices[index]  # Update prevIndex
            
        return count
s = Solution()
print(s.shortestWay("abc", "abcbc"))
print(s.shortestWay("abc", "acdbc"))
print(s.shortestWay("xyz", "xzyxz"))
print(s.shortestWay("aaaaa", "aaaaaaaaaaaaa"))
print(s.shortestWay("adbsc", "addddddddddddsbc"))
