import DoublyLinkedList
__author__ = "Brandon Hardesty"

class Queue:

    def __init__(self):
        """
        Creates a new Queue
        """
        self.queue = DoublyLinkedList.DoublyLinkedList()
    def is_empty(self):
        """
        Test if the Queue is empty
        :return: True or False
        """
        return self.queue.size == 0
    def size(self):
        """
        Gives the size of the Queue
        :return: the number of elements in the queue
        """
        return self.queue.size
    def enqueue(self,value):
        """
        Adds a node object to the front of the queue
        :param value: The value
        :return: nothing
        """
        self.queue.addFront(value)
    def dequeue(self):
        """
        Remove the last object in the queue
        :return: The last value in the queue
        """
        return self.queue.removeRear()



