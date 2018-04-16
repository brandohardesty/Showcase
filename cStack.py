import DoublyLinkedList
__author__ = "Brandon Hardesty"

class Stack:

    def __init__(self):
        """
        Creates a new stack
        """
        self.stack = DoublyLinkedList.DoublyLinkedList()

    def isEmpty(self):
        """
        Test if the stack is empty
        :return: True or false
        """
        return self.stack.size == 0

    def size(self):
        """
        Gives the size of the stack
        :return: The number of elements in the stack
        """
        return self.stack.size
    def push(self,value):
        """
        Adds a node to the rear of the stack
        :param value: The object you want to add
        :return: nothing
        """
        self.stack.addRear(value)
    def pop(self):
        """
        Removes the last item on the stack
        :return: the value of the last item
        """
        if self.isEmpty():
            raise Exception
        return self.stack.removeRear()
    def peek(self):
        """
        Looks at the last item on the stack
        :return: the value of the last item on the stack
        """

        return self.stack.atIndex(self.stack.size-1)


