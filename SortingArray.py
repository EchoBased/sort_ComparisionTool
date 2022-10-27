#Author: Erik Wright

import math
import random
from re import M
import time
import sys
from tkinter import LEFT
from turtle import position, right

#bypass recursion limit for Python needed for quicksort()
#was usefull when quicksort was written recusivly but bugged out on opt 3 if size was larger than 10000
#switched to iterative version of quicksort to get it to work.
#sys.setrecursionlimit(100000)

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min = i

        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        (arr[i], arr[min]) = (arr[min], arr[i])

def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-= 1
        arr[j + 1] = key

def shellSort(arr):
    n = len(arr)
    gap = math.floor(n/2)

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap = math.floor(gap/2)

def merge(arr, l, m ,r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    
    i = 0 
    j = 0 
    k = l 

    while i < n1 and j < n2: 
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
 
        m = l+(r-l)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 
def partition(array,low,high):
    i = ( low - 1 )
    x = array[high]
 
    for j in range(low , high):
        if   array[j] <= x:
 
            i = i+1
            array[i],array[j] = array[j],array[i]
 
    array[i+1],array[high] = array[high],array[i+1]
    return (i+1)
 
# low  --> Starting index,
# high  --> Ending index
def quicksort(array,low,high):
 
    #  auxiliary stack
    size = high - low + 1
    stack = [0] * (size)
 
    top = -1
 
    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high
 
    # Keep popping from stack while is not empty
    while top >= 0:
 
        # Pop high and low
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1
 
        # sorted array
        p = partition( array, low, high )

        # push left side to stack
        if p-1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1

        #  push right side to stack
        if p+1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def printArray(arr):
    n = len(arr)

    for i in range(0,  n):
        print(str(arr[i]) + ' ', end=' ')

    print('\n')

def generateRandomNumbers(cnt, type):
    # This function will generate Integer array of which size is cnt.
    # The range of the generated numbers is 0 ~ cnt
    # type: 1: totally random, 2: sorted_numbers, 3: reverse_sorted_number

    if type == 1:
        arr = [random.randint(1,1000) for i in range (0,cnt)]
        return arr
    elif type == 2:
        arr = [random.randint(1,1000) for i in range (0,cnt)]
        arr.sort()
        return arr
    elif type == 3:
        arr = [random.randint(1,1000) for i in range (0,cnt)]
        arr.sort(reverse=True)
        return arr
    else:
        sys.exit("Not a valid option. Types can be 1, 2 ,3")



if __name__ == '__main__':
    # The parameters from the execution will be used as prameters for the generateRandomNumbers function below.
    # You must receive parameters from the command lines like below.
    # Python3 SortingArray.py 1000000 6 3
    if len(sys.argv) != 4:
        sys.exit("Pass three and only three args. EX: SortingArray.py 1000000 6 3")
    elif len(sys.argv) == 4:
        inAmmount = sys.argv[1]
        sortStyle = sys.argv[2]
        orderStyle = sys.argv[3]
        
        #cast str to int
        outAmmount = int(inAmmount)
        outSS = int(sortStyle)
        outOS = int(orderStyle)

    arr = generateRandomNumbers (outAmmount,outOS)

    if len(arr) < 100:
        print('Before sort: ')
        printArray(arr)

    # Timer Start
    t0 = time.time()
    selector = outSS
	# Sorting method will be provided as the second parameter for main args[2]
	# 1: Bubble Sort
    if selector == 1:
        bubbleSort(arr)
	# 2: Selection Sort
    elif selector == 2:
        selectionSort(arr)
	# 3: Insertion Sort
    elif selector == 3:
        insertionSort(arr)
	# 4: Shell Sort
    elif selector == 4:
        shellSort(arr)#fix float issue
	# 5: Merge Sort
    elif selector == 5:
        n = len(arr)
        mergeSort(arr, 0, n-1)
	# 6: Quick Sort
    elif selector == 6:
       
        n = len(arr)
        quicksort(arr, 0, n-1)
	# Else: Not supported
    else:
        sys.exit("Valid options are 1 through 6. No vaild sort option selected exiting out!")

	#Timer end
    t1 = time.time()
    total = t1-t0
    
	#Print numbers only when the cnt is less than 100
    if len(arr) < 100:
        print('After sort: ')
        printArray(arr)

    #Print elapsed time for sorting.
    print("Time",total)