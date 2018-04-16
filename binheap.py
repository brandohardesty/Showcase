__author__ = 'Bradley N. Miller, David L. Ranum modified by Jack Tompkins'

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def insert(self, k):
        """
        inserts k into the priority queue so the priority is maintained
        :param k:
        :return: None
        """
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def findMin(self):
        """ Finds and returns the minimum value in the priority queue.
        :return: the object with the minimum value
        """
        return self.heapList[1]
          
    def delMin(self):
        """ Removes and returns the minimum value in the priority queue. Catches the potential
        IndexError.
        :return: minimum value in the priority queue, None if attempted on an empty heap
        """
        retval = None
        try:
          retval = self.heapList[1]
          self.heapList[1] = self.heapList[self.currentSize]
          self.currentSize = self.currentSize - 1
          self.heapList.pop()
          self.percDown(1)
        except IndexError:
            pass
        return retval
    
    def isEmpty(self):
        """ Returns True if the priority queue is empty, False otherwise."""
        return self.currentSize == 0

    def size(self):
        """ Returns the current size of the priority queue."""
        return self.currentSize

    def buildPriorityQueue(self, alist):
        """ Builds an otherwise empty priority queue from the list parameter.
        :param alist: A list of comparable objects.
        :return: None
        """
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
          self.percDown(i)
          i = i - 1

    def percUp(self, i):
        """ Percolates an item, at index i, as far up in the tree as it needs to go to maintain the heap property
        :param i: the index of the item
        :return: None
        """
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2
  
    def percDown(self,i):
        """ Invoked by delMin and buildPriorityQueue. Invokes minChild.
        Since the heap property requires that the root of the tree be the smallest item in the tree,
        finding the minimum item is easy.
        The hard part of delMin is restoring full compliance with
        the heap structure and heap order properties after the root has been removed.
        We can restore our heap in two steps.
        First, we will restore the root item by taking the last item in the list and moving it to the root position.
        Moving the last item maintains our heap structure property.
        However, we have probably destroyed the heap order property of our binary heap.
        Second, we will restore the heap order property by pushing the new root node down the tree to its proper position.
        :param i:
        :return: None
        """
        while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
        """ Invoked by percDown. If there is only one child, its index is returned.
        If there are two children, then the smaller childs index is returned.
        :param i: index of the parent
        :return: the index of the minimum child
        """
        if i * 2 + 1 > self.currentSize:
          return i * 2
        else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

def main():
    print('Invoking BinHeap()')
    bh = BinHeap()
    print('Size: {}, isEmpty(): {}, delMin(): {}'.format(bh.size(), bh.isEmpty(), bh.delMin()))
    data = [9,5,6,2,3]
    print('Invoking buildPriorityQueue({}) which invokes percDown from the middle of the list to the top.'.format(data))
    bh.buildPriorityQueue(data)
    x = -5
    print('Invoking insert({0}) which appends {0} to the heap then invokes percUp.'.format(x))
    bh.insert(x)
    print('Size: {}, isEmpty(): {}'.format(bh.size(), bh.isEmpty()))
    print('''while bh.size() > 0: invoking delMin(),
which stores the min value for later return,
places the last element first, reduces the size, pops the end
then invokes percDown''')
    while bh.size() > 0:
        print(bh.delMin())

if __name__ == '__main__':
    main()
