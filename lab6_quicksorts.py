import os
import sys
from urllib.request import urlopen
import matplotlib.pyplot as plt
from time import clock
import math
import random
__author__ = 'Brandon Hardesty'

def plot(data_map, title, xlabel='N', ylabel='time - seconds'):
    """
    Plots the two sets of data (minimum 8 datapoints) in the dictionary data_map using its keys as labels
    :param data_map: a dictionary containing the x data points and two sets of y data points
    :param title: Map heading
    :param xlabel: abscissa axis
    :param ylabel: ordinate axis
    :return: None
    """
    labels = list(data_map.keys())
    plt.title(title)
    x = data_map[labels[0]]
    y1 = data_map[labels[1]]
    y2 =  data_map[labels[2]]
    plt.plot(x, y1, label=labels[1], color='g')
    plt.plot(x,y2, label=labels[2], color='b')

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.text(x[2], y1[2], 'f({0:,}) = {1:.2}\nn = {0:,}'.format(x[2], y1[2]), color='g')  # n, f(n)
    plt.text(x[5], y1[5], 'f({:,}) = {:.2}\n= {:.2}f(n) '.format(x[5], y1[5], y1[5]/y1[2]), color='g')  # n, f(2n)/f(n)

    plt.text(x[0], y2[0], 'f({0:,}) = {1:.2}\nn = {0:,}'.format(x[0], y2[0]), color='b')  # n, f(n)
    plt.text(x[7], y2[7], 'f({:,}) = {:.2}\n= {:.2}f(n) '.format(x[7], y2[7], y2[7] / y2[0]), color='b')  # n, f(8n)/f(n)

    plt.legend()
    plt.show()

def get_from_web(web_addr, save=True):
    """
    Retrieves and saves the resource located at the provided URL
    :param web_addr: URL
    :param save: default Boolean saves to a file in a directory named data
    :return: a list of strs created from space delimited str tokens in the web resource
    """
    response = urlopen(web_addr).read()  # urlopen creates the connection
                                         # read returns a bytes object
    file_name = web_addr[web_addr.rfind('/') + 1:]
    if not os.path.exists('data'):
        os.makedirs('data')
    if save:
        with open('data/' + file_name, 'wb') as f:
            f.write(response)
    
    return response.decode().split()

def quicksort(xlist):
    qsort(xlist, 0, len(xlist)-1)
    
def qsort(xlist, L, R):
    i = L
    j = R
    ip = L + (R - L) // 2  # index of middle element
    p = xlist[ip] # pivot element in the middle
         
    while i <= j:
        while xlist[i] < p: i += 1
        while xlist[j] > p: j -= 1
        if i <= j: # swap and increment i, decrement j
            xlist[i], xlist[j] = xlist[j], xlist[i]
            i += 1
            j -= 1
			
    if L < j:  # sort left list
        qsort(xlist, L, j)
    if i < R:  # sort right list
        qsort(xlist, i, R)

def bquickSort(alist):
   bquickSortHelper(alist,0,len(alist)-1)

def bquickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition2(alist,first,last)

       bquickSortHelper(alist,first,splitpoint-1)
       bquickSortHelper(alist,splitpoint+1,last)


def partition2(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp

   return rightmark
def genData():
    file = open('data.txt','w')

    set1 = [-1*(i**2) for i in range(-50,51)]
    set2 = [i for i in range(50,0-1)]

    for x in range(0,51):
        set2.append(x)


    file.write('Data Set 1\n')
    for x in range(len(set1)):
        file.write(str(set1[x])+'\n')

    file.write('Data Set 2\n')
    for x in range(len(set2)):
        file.write(str(set2[x])+'\n')


    return (set1,set2)

def main(start, data, func, title):
    data_sorted = sorted(data, reverse=True)   
    data_map = {'x':[], 'randomized data':[], 'sorted data':[]}
    print('\n{}'.format(title))
    temp = 0
    temp2 = 0
    step = start
    end = start + 8*step + 1
    for n in range(start, end, step):
        ulist = data[:n]
        slist = data_sorted[:n]
        expected = temp * (n ** 2)
        expected2 = temp2 * (n * math.log10(n))
        
        start1 = clock()
        func(ulist)
        time1 = clock() - start1
        temp2 = time1 / (n * math.log10(n))
        start2 = clock()
        func(slist)
        time2 = clock() - start2
        temp = time2 / (n**2)


        data_map['x'].append(n)
        data_map['randomized data'].append(time1)
        data_map['sorted data'].append(time2)

    x = data_map['x']
    y1 = data_map['randomized data']
    y2 = data_map['sorted data']
    analyze_data(x, y1, 'green')
    analyze_data(x, y2, 'blue')
        
    plot(data_map, title)



def analyze_data(x, y, color='green'):
    if color is 'blue':
        print('Sorted {}'.format(color))
    else:
        print('Unsorted {}'.format(color))
    print('f({0:,}) = {1:.2}, n = {0:,}'.format(x[2], y[2]))
    print('f({:,}) = {:.2}, = {:.2}f(n) '.format(x[5], y[5], y[5] / y[2]))
    print('f({0:,}) = {1:.2}, n = {0:,}'.format(x[0], y[0]))
    print('f({:,}) = {:.2}, = {:.2}f(n) '.format(x[7], y[7], y[7] / y[0]))
    if y[5]/y[2] < 1.5 or y[7]/y[0] < 6 :  # output ratio for doubled input less than double
        print('The {} graph is better than linear? \n \
              Expected: f(2n) ≅ 2*f(n), f(8n) ≅ 8*f(n)'.format(color))
    elif round(y[5]/y[2]) == 2 or round(y[7]/y[0]) == 8:  # output ratio for doubled input is also double
        print('The {} graph appears to be linear. \n \
              Expected: f(2n) ≅ 2*f(n), f(8n) ≅ 8*f(n)'.format(color))
    elif round(y[5]/y[2])  >= 3 and round(y[7]/y[0]) > 32:
        # output ratio for double input is quadratic, for 8*input it is 64f(n)
        print('****The {} graph may be quadratic. \n \
              Expected: f(2n) ≅ 4*f(n), f(8n) ≅ 64*f(n) ****\n'.format(color))
    elif round(y[5]/y[2])  >= 4 or round(y[7]/y[0])  >= 64:
        # output ratio for doubled input is quadratic, for 8 * input it is 64f(n)
        print('**************The {} graph appears to be quadratic. \n \
              Expected: f(2n) ≅ 4*f(n), f(8n) ≅ 64*f(n) **************\n'.format(color))


def conclusions():
    ans1 = """ The list is being partitioned the maximum amount of times if you pivot on the endpoints of the dataset. The reason the sort runs the maximum amount of times is because the list only gets smaller by one each run. """
    print('\nDiscussion regarding the dataset size limitations exhibited using "quickSort - first element pivot" in Step 1.\n\t{}'.format(ans1))
    ans2 = """ Actual (6.2e-05)/30^2 = (expected time)/60^2" Expected Time calculation = 2.48e-4 and the actual time was 2.2e-4 so the calculations are accurate."""
    print('Calculations for Step 2 showing actual vs expected performance of "quicksort - middle pivot"\n\t{}'.format(ans2))
    ans3 = """ I generated a data set where the data increased until the middle was the maximum value. The decreased from the middle value to the end of the data set. This allows for decreasing the list size by 1 each run."""
    print('Design particulars for your datasets created in Step 2.\n\t{}'.format(ans3))
    ans4 = """ Yes, my generated data set degrades the run time to n^2 because it results in the maximum number of runs."""
    print('Does the middle pivot solve the quicksort degradation problem?\n\t{}'.format(ans4))


if __name__ == '__main__':    
    data = get_from_web('http://people.uncw.edu/tompkinsj/231/resources/dictionary.txt')
    print("""This Lab test various quicksort algorithms using particular datasets to show graphically that the 
    algorithm may degrade to O(n**2) given the right conditions.""")
    print("""In the second part, we attempt to degrade quicksort with middle pivot using different combinations of  
    datasets since it efficiently handled presorted data sets.""")
    print("Initial dataset: type {}, type element {}, first element {}, last element {}, size {:,}.".
          format(type(data), type(data[0]), data[0], data[-1], len(data)))
    main(50, data, bquickSort, 'Unsorted vs Sorted Quick Sorts - middle pivot')
    start_size = 50  # invoke main with a start_size appropriate for the recursive first pivot quickSort, same data, new function name, and new title
    main(start_size,data, quicksort, 'Unsorted vs Sorted Quick Sorts - first element pivot')
    
    # populate data with the return value from your dataset building function which builds and saves dataset to data folder
    title = ' '  # invoke main with a modified title
    datatup = genData()
    main(10,datatup[0], bquickSort, 'Unsorted {} vs Sorted {} - middle pivot'.format(title,title))
    conclusions()
    
