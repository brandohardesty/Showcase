__author__ = 'Bradley N. Miller, David L. Ranum modified by Jack Tompkins and student'

import MixedFraction
import random
import math
import binheap
import csv
import time
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class Queue23:
    def __init__(self):
        self.head = None

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def isEmpty(self):
        """ Returns True if the priority queue is empty, False otherwise."""
        return self.head is None

    def size(self):
        """ Returns the current size of the priority queue."""
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.getNext()
        return count

    def insert(self, k):
        self.add(k)

    def findMin(self):
        """ Finds and returns the minimum value in the priority queue.
        :return: the object with the minimum value
        """
        return self.head.getData()

    def delMin(self):
        """ Removes and returns the minimum value in the priority queue. Catches the potential
        IndexError.
        :return: minimum value in the priority queue, None if attempted on an empty heap
        """
        retval = None
        try:
            retval = self.head.getData()
            self.head = self.head.next


        except IndexError:
            return None

        return retval

    def buildPriorityQueue(self, alist):
        """ Builds an otherwise empty priority queue from the list parameter.
        :param alist: A list of comparable objects.
        :return: None
        """

        blist = list(alist)
        blist.sort()
        pNode = Node(blist[0])
        self.head = pNode
        del blist[0]
        for i in range(len(blist)):
            t = Node(blist[0])
            pNode.next = t
            pNode = t
            del blist[0]










class Queue12:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        """ Returns True if the priority queue is empty, False otherwise."""
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        """ Returns the current size of the priority queue."""
        return len(self.items)

    def insert(self, k):
        """
        inserts k into the priority queue so the priority is maintained
        :param k:
        :return: None
        """
        self.items.append(k)
        self.items.sort()

    def findMin(self):
        """ Finds and returns the minimum value in the priority queue.
        :return: the object with the minimum value
        """
        return self.items[0]

    def delMin(self):
        """ Removes and returns the minimum value in the priority queue. Catches the potential
        IndexError.
        :return: minimum value in the priority queue, None if attempted on an empty heap
        """
        retval = None
        try:
            retval = self.items[0]
            del self.items[0]
        except IndexError:
            return None
        return retval

    def buildPriorityQueue(self, alist):
        """ Builds an otherwise empty priority queue from the list parameter.
        :param alist: A list of comparable objects.
        :return: None
        """
        self.items = alist
        self.items.sort()
def generateDataSet():
    randomMixedFractions = list()
    for i in range(40000):
        randomMixedFractions.append(MixedFraction.MixedFraction(random.randint(1,100),random.randint(1,100)))

    dataSets = {"10k":[],"20k":[],"30k":[],"40k":[]}
    dataSets["10k"] = randomMixedFractions[:10000]
    dataSets["20k"] = randomMixedFractions[:20000]
    dataSets["30k"] = randomMixedFractions[:30000]
    dataSets["40k"] = randomMixedFractions[:40000]

    return dataSets
def getData(dataList):
    minimum = min(dataList)
    maximum = max(dataList)
    totalListVal = MixedFraction.MixedFraction(0,1)
    for i in dataList:
        totalListVal += i
    avg = totalListVal/MixedFraction.MixedFraction(len(dataList),1)
    delta = MixedFraction.MixedFraction(0,1)
    deltaList = list()
    realAvg = 0
    for i in range(len(dataList)):
        delta = dataList[i] - avg
        if(delta == MixedFraction.MixedFraction(0,1)):
            realAvg = dataList[i]
            deltaList.append(abs(delta))
        else:
            deltaList.append(abs(delta))
    realAvg = dataList[deltaList.index(min(deltaList))]

    return (minimum,maximum,realAvg)

    

def timeOperations(data):



    listQ = Queue12()
    linkedQ = Queue23()
    binQ = binheap.BinHeap()
    keys = ["10k","20k","30k","40k"]

    with open("table.csv", "w") as file:
        nList = [10000, 20000, 30000, 40000]
        writer = csv.writer(file)
        writer.writerow(["listQ", "linkedQ", "binQ"])
        for i in keys:
            listQ.buildPriorityQueue(data[i])
            linkedQ.buildPriorityQueue(data[i])
            binQ.buildPriorityQueue(data[i])





            st = time.clock()
            listQ.findMin()
            sp = time.clock()
            listQT = sp - st


            st = time.clock()
            linkedQ.findMin()
            sp = time.clock()
            linkedQT = sp - st


            st = time.clock()
            binQ.findMin()
            sp = time.clock()
            binQT = sp - st

            writer.writerow([listQT,linkedQT,binQT])

    with open("insert.csv", "w") as file:
        nList = [10000, 20000, 30000, 40000]
        insertWriter = csv.writer(file)
        insertWriter.writerow(["listQ", "linkedQ", "binQ"])
        for i in keys:
            listQ.buildPriorityQueue(data[i])
            linkedQ.buildPriorityQueue(data[i])
            binQ.buildPriorityQueue(data[i])
            avgE = getData(data[i])[2]

            st = time.clock()
            listQ.insert(avgE)
            sp = time.clock()
            listQT = sp - st


            st = time.clock()
            linkedQ.insert(avgE)
            sp = time.clock()
            linkedQT = sp - st


            st = time.clock()
            binQ.insert(avgE)
            sp = time.clock()
            binQT = sp - st
            insertWriter.writerow([listQT,linkedQT,binQT])



    with open("del.csv", "w") as file:
        nList = [10000, 20000, 30000, 40000]
        delWriter = csv.writer(file)
        delWriter.writerow(["listQ", "linkedQ", "binQ"])
        for i in keys:
            listQ.buildPriorityQueue(data[i])
            linkedQ.buildPriorityQueue(data[i])
            binQ.buildPriorityQueue(data[i])

            st = time.clock()
            listQ.delMin()
            sp = time.clock()
            listQT = sp - st

            st = time.clock()
            linkedQ.delMin()
            sp = time.clock()
            linkedQT = sp - st

            st = time.clock()
            binQ.delMin()
            sp = time.clock()
            binQT = sp - st

            delWriter.writerow([listQT,linkedQT,binQT])






















    #finding minimum test 10k through 40k




def main():
    timeOperations(generateDataSet())
    



    pass


if __name__ == '__main__':
    main()
