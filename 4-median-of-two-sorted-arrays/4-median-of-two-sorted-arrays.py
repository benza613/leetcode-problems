class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # nums1 is always shorter than nums2, O(1)
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m = len(nums1) #shorter one
        n = len(nums2) #longer one
        
        # edge cases - improves time performance (should still work if commented)
        if not nums1 or nums1[0] >= nums2[-1]:
            nums = nums2 + nums1
            return (nums[(m+n)//2] + nums[(m+n-1)//2])/2
        
        if nums1[-1] <= nums2[0]:
            nums = nums1 + nums2
            return (nums[(m+n)//2] + nums[(m+n-1)//2])/2
        
        # find smaller median equals to find the num that is larger than (m+n-1)//2 items
        
        low1 = 0
        high1 = m
        
        # following these loops, low1/high1 will return the idx right larger than the smaller median in the shorter list 
        # low1-1 should be the smaller median or the largest number smaller than median in list1 (low1 == 0 if do not exist)
        # as the smaller list is cut into half each time, the complexity of the loop would be bounded by log(min(n,m))
        while low1 < high1:
            
            mid1 = (high1+low1)//2
            idx2 = (m+n-1)//2 - mid1

            ref = nums2[idx2]

            if nums1[mid1] > ref:
                high1 = mid1
            else:
                low1 = mid1 + 1 # so that largest number smaller or equal to the median would be always at left
        
        # if the smaller median is not in nums1, then idx2 in nums2 would be the smaller median
        idx2 = (m+n-1)//2 - low1

        if idx2 < 0:
            smaller = nums1[low1-1]
        elif low1 - 1 < 0:
            smaller = nums2[idx2]
        else:
            smaller = max(nums2[idx2], nums1[low1-1])
        
        # when there is only one median, completed
        if (m+n) % 2 == 1:
            return smaller
        
        # the smaller one between idx2+1 in nums2 and low1 in nums1, if both exist, would be the larger median
        if idx2 + 1 >= n:
            larger = nums1[low1]
        elif low1 >= m:
            larger = nums2[idx2+1]
        else:
            larger = min(nums2[idx2+1], nums1[low1])
        return (smaller+larger)/2
        
        
    