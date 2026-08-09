class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MyCircularQueue:

    def __init__(self, k: int):
        self.size=k
        self.count=0
        self.head=None
        self.tail=None

        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node=Node(value)
        if self.isEmpty():
            self.head=self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node  
        self.count+=1
        return True      

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head=self.head.next
        self.count-=1
        if self.isEmpty():
            self.tail=None
        return True
        

    def Front(self) -> int:
        return self.head.val if self.head else -1
        

    def Rear(self) -> int:
        return self.tail.val if self.tail else -1
        

    def isEmpty(self) -> bool:
        return self.count==0
        

    def isFull(self) -> bool:
        return self.count==self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()