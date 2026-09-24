import heapq

class MedianFinder:

    def __init__(self):
        # max heap (store as negative values for Python's min-heap)
        self.small = []
        # min heap
        self.large = []

    def addNum(self, num: int) -> None:
        # Push to max heap (small)
        heapq.heappush(self.small, -num)

        # Balance: largest of small goes to large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Ensure size property: small can have one more element than large
        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        # If odd, median is top of small
        if len(self.small) > len(self.large):
            return -self.small[0]
        # If even, average of tops
        return (-self.small[0] + self.large[0]) / 2
