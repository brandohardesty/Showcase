__author__ = "Brandon Hardesty"


class DoublyLinkedNode:
    """ A single node in a doubly-linked list.
        Contains 3 instance variables:
            data: The value stored at the node.
            prev: A pointer to the previous node in the linked list.
            next: A pointer to the next node in the linked list.
    """

    def __init__(self, value):
        """
        Initializes a node by setting its data to value and
        prev and next to None.
        :return: The reference for self.
        """
        self.data = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """
    The doubly-linked list class has 3 instance variables:
        head: The first node in the list.
        tail: The last node in the list.
        size: How many nodes are in the list.
    """

    def __init__(self):
        """
        The constructor sets head and tail to None and the size to zero.
        :return: The reference for self.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def addFront(self, value):
        """
        Creates a new node (with data = value) and puts it in the
        front of the list.
        :return: None
        """
        newNode = DoublyLinkedNode(value)
        if (self.size == 0):
            self.head = newNode
            self.tail = newNode
            self.size = 1
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            self.size += 1

    def addRear(self, value):
        """
        Creates a new node (with data = value) and puts it in the
        rear of the list.
        :return: None
        """
        newNode = DoublyLinkedNode(value)
        if (self.size == 0):
            self.head = newNode
            self.tail = newNode
            self.size = 1
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
            self.size += 1

    def removeFront(self):
        """
        Removes the node in the front of the list.
        :return: The data in the deleted node.
        """
        value = self.head.data
        self.head = self.head.next
        if self.head != None:
            self.head.prev = None
        self.size -= 1
        return value

    def removeRear(self):
        """
        Removes the node in the rear of the list.
        :return: The data in the deleted node.
        """
        value = self.tail.data
        self.tail = self.tail.prev
        if self.tail != None:
            self.tail.next = None
        self.size -= 1
        return value

    def printItOut(self):
        """
        Prints out the list from head to tail all on one line.
        :return: None
        """
        temp = self.head
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def printInReverse(self):
        """
        Prints out the list from tail to head all on one line.
        :return: None
        """
        temp = self.tail
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.prev
        print()


    def atIndex(self, index):
        """
        Retrieves the data of the item at index.
        :param index: The index of the item to retrieve.
        :return: Returns the data of the item.
        """
        count = 0
        temp = self.head
        while count < index:
            count += 1
            temp = temp.next
        if not temp:
            return None
        return temp.data
    def indexOf(self,value):
        for i in range(self.size):
            if (value == self.atIndex(i)):
                return i
        return -1
    def insertAt(self,index,value):
        newNode = DoublyLinkedNode(value)
        temp = self.head

        for i in range(index):
            temp = temp.next

        if(index == 0):
            self.addFront(value)
        elif(index == (self.size)):
            self.addRear(value)
        else:
            temp.prev.next = newNode
            newNode.prev = temp.prev
            temp.prev = newNode
            newNode.next = temp
        self.size += 1
    def removeAt(self,index):
        temp = self.head

        for i in range(index):
            temp = temp.next

        if(index == 0):
            return self.removeFront()

        elif(index == (self.size-1)):
            return self.removeRear()
        else:
            print(self.size)
            value = temp.data
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
        self.size -= 1
        return value
















def main():
    dll = DoublyLinkedList() 
    dll.addRear(5) 
    dll.addRear(2) 
    dll.addRear(25) 
    dll.addRear(-4)
    dll.insertAt(2,7) 
    dll.printItOut()

    x = dll.removeAt(2)
    dll.printItOut()
    print("\tThe item removed was {}.".format(x))
    x = dll.removeAt(0)
    dll.printItOut()
    print("\tThe item removed was {}.".format(x))
    x = dll.removeAt(2)
    dll.printItOut()
    print("\tThe item removed was {}.".format(x))

    # optionally
    print()
    dll = DoublyLinkedList() 
    dll.addRear(1) 
    dll.addRear(2) 
    dll.addRear(4) 
    dll.addRear(25) 
    dll.addRear(35) 
    dll.printItOut()
    for i in range(dll.size):
        y = dll.atIndex(i)
        yIndex = dll.indexOf(y)
        print('The value at index {:d} is {} for which indexOf({}) returned {}.'.format(i,y,y,yIndex))
    print('indexOf(-10) is {}'.format(dll.indexOf(-10)))
    print('The dll size is {}.'.format(dll.size))


if __name__ == '__main__':
    main()
