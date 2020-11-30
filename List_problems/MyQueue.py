# Your MyQueue object will be instantiated and called as such:
# MyQueue queue = new MyQueue();
# queue.push(1);
# queue.push(2);
# queue.peek();  // return 1
# queue.pop();   // return 1
# queue.empty(); // return false

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.data.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.data.pop(0)

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.data[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.data.__len__() == 0


if __name__ == '__main__':
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print(queue.peek())
    print(queue.pop())
    print(queue.empty())
