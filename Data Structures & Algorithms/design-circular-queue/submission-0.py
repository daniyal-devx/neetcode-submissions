class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k  # Array of fixed size
        self.size = k
        self.front = 0        # Points to first element
        self.rear = -1        # Points to last element
        self.count = 0        # Number of elements currently in queue

    def enQueue(self, value: int) -> bool:
        """Add an element to the queue. Return True if successful."""
        if self.isFull():
            return False
        
        # Move rear forward (with wrap-around)
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        """Remove an element from the queue. Return True if successful."""
        if self.isEmpty():
            return False
        
        # Move front forward (with wrap-around)
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True

    def Front(self) -> int:
        """Get the front element of the queue."""
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        """Get the last element of the queue."""
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        """Check if the queue is empty."""
        return self.count == 0

    def isFull(self) -> bool:
        """Check if the queue is full."""
        return self.count == self.size
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()