from collections import deque
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.queue = deque()
        self.count = Counter()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while self.queue and self.count[self.queue[0]] > 1:
            self.queue.popleft()
        return self.queue[0] if self.queue else -1
        

    def add(self, value: int) -> None:
        self.count[value] += 1
        if self.count[value]==1:
            self.queue.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
