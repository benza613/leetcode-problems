import heapq

class MedianFinder:

    def __init__(self):
        
        # max heap -> lower half of elems 
        self.lo = []
        
        # min heap -> upper half of elems
        # multiply elems by -1 when push-pop
        self.hi = []
        
        heapq.heapify(self.lo);
        heapq.heapify(self.hi);
        

    def addNum(self, num: int) -> None:
        
        # 1. add to max heap 
        heapq.heappush(self.lo, num)
        
        # 2. balance hi and then low
        greatest_lo = heapq.heappop(self.lo)
        heapq.heappush(self.hi, -greatest_lo)
        
        # 3. check if len exceeded => low must ALWAYS be equal or 1 greater than high
        if len(self.lo) < len(self.hi):
            lowest_hi = heapq.heappop(self.hi)
            heapq.heappush(self.lo, -lowest_hi)
        

    def findMedian(self) -> float:
        
        if len(self.lo) == len(self.hi):
            return (self.lo[0] + -self.hi[0])/2
        else:
            return self.lo[0]
        
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()