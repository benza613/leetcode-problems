from typing import List

# https://leetcode.com/problems/check-array-formation-through-concatenation/


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:

        idx = 0

        while idx < len(arr):
            el = arr[idx]
            el_found = False
            pc_size = 0

            for piece in pieces:

                if set([el]).issubset(set(piece)):
                    el_found = True

                    if piece != arr[idx : len(piece) + idx]:
                        return False
                    else:
                        pc_size = len(piece)
                        #print("\t el", el)
                        break

            if el_found == False:
                return False

            idx += pc_size

        return True


x = Solution()

print(x.canFormArray([85], [[85]]))
print(x.canFormArray([15, 88], [[88], [15]]))
print(x.canFormArray([49, 18, 16], [[16, 18, 49]]))
print(x.canFormArray([91, 4, 64, 78], [[78], [4, 64], [91]]))
print(x.canFormArray([1, 3, 5, 7], [[2, 4, 6, 8]]))
