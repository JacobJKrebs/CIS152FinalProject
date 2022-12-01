import QueueEmptyException as qec
import QueueFullException as qfc

"""
This program is a slight alteration to my queue application to allow for items to have 
priority and to be deleted based on that priority.

Jacob Krebs

Oct 10 22
"""

class Queue:
    def __init__(self, max_size=10):
        self.head = -1
        self.tail = -1
        self.size = 0
        self.max_size = max_size  # Determines max size of queue
        self.items = [x for x in range(max_size)]  # Creates slots for items in queue

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def enqueue(self, item, priority):
        if not self.is_full():
            if self.head == -1:
                self.head += 1
                self.tail += 1
            if self.size == 0:
                self.items[self.head] = f"{item}_{priority}"
            else:
                self.tail += 1
                self.items[self.tail] = f"{item}_{priority}"
            self.size += 1
        else:
            raise qfc.QueueFullException()


        pass

    def dequeue(self):
        removed = False #Flag to stop checking so the whole list doesn't self-destruct
        if not self.is_empty(): #this code is checking the priority, denoted by the last character in the string.
            iterator = 0
            for i in self.items:
                if str(i)[-1] == "1" and removed == False:
                    self.items.pop(iterator)
                    removed = True
                iterator += 1
            iterator = 0
            for i in self.items:
                if str(i)[-1] == "2" and removed == False:
                    self.items.pop(iterator)
                    removed = True
                iterator += 1
            iterator = 0
            for i in self.items:
                if str(i)[-1] == "3" and removed == False:
                    self.items.pop(iterator)
                    removed = True
                iterator += 1
            iterator = 0
            for i in self.items:
                if str(i)[-1] == "4" and removed == False:
                    self.items.pop(iterator)
                    removed = True
                iterator += 1
            iterator = 0
            for i in self.items:
                if str(i)[-1] == "5" and removed == False:
                    self.items.pop(iterator)
                    removed = True
                iterator += 1
            iterator = 0
            for i in self.items:
                if str(i)[-1] == "6" and removed == False:
                    self.items.pop(iterator)
                    removed = True
                iterator += 1
            iterator = 0
            for i in self.items:
                if str(i)[-1] == "7" and removed == False:
                    self.items.pop(iterator)
                    removed = True
                iterator += 1
            iterator = 0
            for i in self.items:
                if str(i)[-1] == "8" and removed == False:
                    self.items.pop(iterator)
                    removed = True
                iterator += 1
            iterator = 0
            for i in self.items:
                if str(i)[-1] == "9" and removed == False:
                    self.items.pop(iterator)
                    removed = True
                iterator += 1
            iterator = 0


            # item_str = self.items[self.head]
            # self.items[self.head] = 0
            # for x in range(self.size - 1):
            #     self.items[x] = self.items[x + 1]

            # Above code commented out since we really only need to check for priority and pop
            # at the correct index
        else:
            raise qec.QueueEmptyException()
        self.size -= 1
        self.tail -= 1
        return

    def peek(self):
        if not self.is_empty():
            item_str = f"{self.items[self.head]}"
        else:
            raise qec.QueueEmptyException()
        return item_str

    def size_of(self):
        return self.size

    def print_queue(self):
        stack_str = ""
        if not self.is_empty():
            for x in range(self.size):
                stack_str += str(self.items[x]) + "\n"
            return stack_str;  # Possibly you will remove this line, this is for running Unit Tests before writing code
        else:
            stack_str = "Queue is Empty"
            return stack_str


# a = Queue()
# a.enqueue("Test","1")
# a.enqueue("Test2", "2")
# a.enqueue("test3", "3")

# print(a.print_queue())
# a.dequeue()
# print(a.print_queue())
# a.dequeue()
# print(a.print_queue())
# print(a.peek())
# a.dequeue()
# print(a.print_queue())