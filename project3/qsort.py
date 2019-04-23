import time
import random

import sys

sys.setrecursionlimit(1500000000)


def insertionSort(array):  # insertion sort function
    for j in range(1, len(array)):  # 10.000 (array length) times loop
        key = array[j]
        i = j - 1
        while (i > -1) and key < array[i]:  # checking values lower or not
            array[i + 1] = array[i]  # transform locations
            i = i - 1
        array[i + 1] = key
    return array


def mergeSort(array):  # merge sort function
    if len(array) > 1:  # if it is 1 it cannot split
        mid = len(array) // 2  # splitting into middle
        lefthalf = array[:mid]  # lefthalf of list
        righthalf = array[mid:]  # righthalf of list

        # recursion splitting all the list
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):  # checking sort lower
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]  # make it lefthalf
                i = i + 1
            else:
                array[k] = righthalf[j]  # make it right half
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            array[k] = lefthalf[i]  # make it left half
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            array[k] = righthalf[j]  # make it right half
            j = j + 1
            k = k + 1


def partition(arr, low, high):
    i = (low - 1)  # its needed because of changed values
    pivot = arr[high]  # pivot is last value of array

    for j in range(low, high):

        if arr[j] <= pivot:
            i += 1  # increment i by 1
            arr[i], arr[j] = arr[j], arr[i]  # swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # swap
    return i + 1  # return value as pi


def quickSort(arr, low, high):
    if low < high:  # basic logic need to start algorithm
        pi = partition(arr, low, high)  # pull the value from partition function
        quickSort(arr, low, pi - 1)  # recursion whenever low greater than pi-1 or equal
        quickSort(arr, pi + 1, high)  # recursion again


def partition_2(arr, low, high):
    pivot = arr[low]  # this time first value is pivot
    while True:  # because of that continous loop
        while arr[low] < pivot:
            low += 1  # increment by 1 until equals to pivot
        while arr[high] > pivot:
            high -= 1  # decrement by 1 until equals to pivot
        if low < high:
            if arr[low] == arr[high]:  # if it is equal return high as pi, or it could be low
                return high
            arr[low], arr[high] = arr[high], arr[low]  # swap low and high
        else:
            return high  # return high value as pi


def quickSort_2(arr, low, high):  # this is second function, first one is pivot
    if low < high:
        pi = partition_2(arr, low, high)
        if pi > 1:
            quickSort_2(arr, low, pi - 1)  # if pi greater than 1, decrement pi by 1 and call the function again
        if (pi + 1) < high:
            quickSort_2(arr, pi + 1, high)  # increment pi by 1 until its equal to high


# ------------------------------------------------------------
# Somehow this method doesn't work on python
# ------------------------------------------------------------
def med3(arr, low, high):
    mid = ((low + high) / 2)
    mid = int(mid)
    if arr[mid] < arr[low]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[high] < arr[low]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[high] < arr[mid]:
        arr[mid], arr[high] = arr[high], arr[mid]
    arr[mid], arr[high - 1] = arr[high - 1], arr[mid]
    return arr[high - 1]


def partition_3(arr, low, high, pi):
    left = low
    right = high - 1
    while True:
        while arr[left] < pi:
            left = left + 1
        while arr[right] > pi:
            right = right - 1
        if left >= right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[left], arr[right - 1] = arr[right - 1], arr[left]
    return left


def manualSort(arr, low, high):
    size = high - low + 1
    if size <= 1:
        return
    if size == 2:
        if arr[low] > arr[high]:
            arr[low], arr[high] = arr[high], arr[low]
            return
    else:
        if arr[low] > arr[high - 1]:
            arr[low], arr[high - 1] = arr[high - 1], arr[low]
        if arr[low] > arr[high]:
            arr[low], arr[high] = arr[high], arr[low]
        if arr[high - 1] > arr[high]:
            arr[high - 1], arr[high] = arr[high], arr[high - 1]


def quickSort_3(arr, low, high):
    size = high - low + 1
    if size <= 3:
        manualSort(arr, low, high)
    else:
        med = med3(arr, low, high)
        partition = partition_3(arr, low, high, med)
        quickSort_3(arr, low, partition - 1)
        quickSort_3(arr, partition + 1, high)


# ------------------------------------------------------------

def median(a, b, c):  # finding median which is a positive value
    if (a - b) * (c - a) >= 0:
        return a

    elif (b - a) * (c - b) >= 0:
        return b

    else:  # if all negative then return c value
        return c


def partition_median(array, low, high):  # Method to partition around the median
    left = array[low]  # left hand
    right = array[high - 1]  # right hand
    length = high - low  # finding length obviously
    if length % 2 == 0:  # this is because of array indicies problem of python3, it was hard to find
        middle = array[low + int(length / 2) - 1]  # saving middle value but integer indicies
    else:
        middle = array[int(low + length / 2)]  # same but exact middle point
    pivot = median(left, right, middle)  # calling median for saving pivot value, middle
    pi = array.index(pivot)  # only works if all values in array unique it means for example , arr[5}
    array[pi] = array[low]  # swapping ex; arr[arr[5]] with arr[0] --> arr[22] equals arr[0}
    array[low] = pivot
    i = low + 1  # incrementation
    for j in range(low + 1, high):
        if array[j] < pivot:  # swapping them until highest element
            array[j], array[i] = array[i], array[j]  # swap
            i += 1
    array[low], array[i - 1] = array[i - 1], array[low]  # swap
    return i - 1  # return value as pi variable


def quicksort_median(array, low, high):  # Median of three method

    if low < high:  # basic logic, if it is false there will be nothing to change
        pi = partition_median(array, low, high)  # calling partition method and saving value of pivot
        quicksort_median(array, low, pi)  # recursion
        quicksort_median(array, pi + 1, high)  # recursion


def heapsort(aList):
    # convert aList to heap
    length = len(aList) - 1
    leastParent = length // 2
    for i in range(leastParent, -1, -1):
        moveDown(aList, i, length)

    # flatten heap into sorted array
    for i in range(length, 0, -1):
        if aList[0] > aList[i]:
            swap(aList, 0, i)
            moveDown(aList, 0, i - 1)


def moveDown(aList, first, last):
    largest = 2 * first + 1
    while largest <= last:
        # right child exists and is larger than left child
        if (largest < last) and (aList[largest] < aList[largest + 1]):
            largest += 1

        # right child is larger than parent
        if aList[largest] > aList[first]:
            swap(aList, largest, first)
            # move down to largest child
            first = largest;
            largest = 2 * first + 1
        else:
            return  # force exit


def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp


suminstime = 0
summertime = 0
sumqtime = 0
sumq2time = 0
sumq3time = 0
sumhtime = 0
suminstimeR = 0
summertimeR = 0
sumqtimeR = 0
sumq2timeR = 0
sumq3timeR = 0
sumhtimeR = 0
x = []
x1 = []  # insertion sort
x2 = []  # merge sort
x3 = []  # quicksort1
x4 = []  # quicksort2
x5 = []  # quicksort3
x6 = []  # heapsort
for k in range(1, 6):
    # for j in range(0, 10000):  # its not 100.000 because in python insertion sort is too slow
    #     num = random.randint(1, 2000000)  # picking between 1-200000 numbers value into num variable
    # x.append(num)  # adding num value to array
    with open('originalList' + str(k) + '.txt', 'r') as filehandle:  # reading original lists
        # for listitem in x:
        #     filehandle.write('%s\n' % listitem)
        for line in filehandle:
            currentPlace = int(line[:-1])
            x1.append(currentPlace)  # adding items into array
            x2.append(currentPlace)  # adding items into array
            x3.append(currentPlace)  # adding items into array
            x4.append(currentPlace)  # adding items into array
            x5.append(currentPlace)  # adding items into array
            x6.append(currentPlace)  # adding items into array

    n = len(x3)
    i_start = int(round(time.time() * 1000))  # timer start
    insertionSort(x1)  # sort function start
    i_stop = int(round(time.time() * 1000))  # timer stop
    suminstime += (i_stop - i_start)
    itime = str(i_stop - i_start)  # calculate time difference between start and stop time
    with open('i-seed' + str(k) + '.txt', 'w') as filehandle:  # write sorted list into txt file
        filehandle.write('%s ms..\n' % itime)
        for listitem in x1:
            filehandle.write('%s\n' % listitem)
    m_start = int(round(time.time() * 1000))  # timer start
    mergeSort(x2)  # sort function start
    m_stop = int(round(time.time() * 1000))  # timer stop
    summertime += (m_stop - m_start)
    mtime = str(m_stop - m_start)  # calculate time difference between start and stop time
    with open('m-seed' + str(k) + '.txt', 'w') as filehandle:  # write sorted list into txt file
        filehandle.write('%s ms..\n' % mtime)
        for listitem in x2:
            filehandle.write('%s\n' % listitem)
    q1_start = int(round(time.time() * 1000))  # timer start
    quickSort(x3, 0, n - 1)
    q1_stop = int(round(time.time() * 1000))  # timer stop
    sumqtime += (q1_stop - q1_start)
    q1time = str(q1_stop - q1_start)  # calculate time difference between start and stop time
    with open('q1-seed' + str(k) + '.txt', 'w') as filehandle:  # write sorted list into txt file
        filehandle.write('%s ms..\n' % q1time)
        for listitem in x3:
            filehandle.write('%s\n' % listitem)
    q2_start = int(round(time.time() * 1000))  # timer start
    quickSort_2(x4, 0, n - 1)
    q2_stop = int(round(time.time() * 1000))  # timer stop
    sumq2time += (q2_stop - q2_start)
    q2time = str(q2_stop - q2_start)  # calculate time difference between start and stop time
    with open('q2-seed' + str(k) + '.txt', 'w') as filehandle:  # write sorted list into txt file
        filehandle.write('%s ms..\n' % q2time)
        for listitem in x4:
            filehandle.write('%s\n' % listitem)
    q3_start = int(round(time.time() * 1000))  # timer start
    quicksort_median(x5, 0, n)
    q3_stop = int(round(time.time() * 1000))  # timer stop
    sumq3time += (q3_stop - q3_start)
    q3time = str(q3_stop - q3_start)  # calculate time difference between start and stop time
    with open('q3-seed' + str(k) + '.txt', 'w') as filehandle:  # write sorted list into txt file
        filehandle.write('%s ms..\n' % q3time)
        for listitem in x5:
            filehandle.write('%s\n' % listitem)
    q1_start = int(round(time.time() * 1000))  # timer start
    quickSort(x3, 0, n - 1)
    q1_stop = int(round(time.time() * 1000))  # timer stop
    sumqtime += (q1_stop - q1_start)
    q1time = str(q1_stop - q1_start)
    with open('q1-seed-sorted' + str(k) + '.txt', 'w') as filehandle:  # write sorted list into txt file
        filehandle.write('%s ms..\n' % q1time)
        for listitem in x3:
            filehandle.write('%s\n' % listitem)
    q2_start = int(round(time.time() * 1000))  # timer start
    quickSort_2(x4, 0, n - 1)
    q2_stop = int(round(time.time() * 1000))  # timer stop
    sumq2time += (q2_stop - q2_start)
    q2time = str(q2_stop - q2_start)
    with open('q2-seed-sorted' + str(k) + '.txt', 'w') as filehandle:  # write sorted list into txt file
        filehandle.write('%s ms..\n' % q2time)
        for listitem in x4:
            filehandle.write('%s\n' % listitem)
    q3_start = int(round(time.time() * 1000))  # timer start
    quicksort_median(x5, 0, n)
    q3_stop = int(round(time.time() * 1000))  # timer stop
    sumq3time += (q3_stop - q3_start)
    q3time = str(q3_stop - q3_start)
    with open('q3-seed-sorted' + str(k) + '.txt', 'w') as filehandle:  # write sorted list into txt file
        filehandle.write('%s ms..\n' % q3time)
        for listitem in x5:
            filehandle.write('%s\n' % listitem)
    h_start = int(round(time.time() * 1000))  # timer start
    heapsort(x6)
    h_stop = int(round(time.time() * 1000))  # timer stop
    sumhtime += (h_stop - h_start)
    htime = str(h_stop - h_start)
    with open('h-seed-sorted' + str(k) + '.txt', 'w') as filehandle:  # write sorted list into txt file
        filehandle.write('%s ms..\n' % htime)
        for listitem in x6:
            filehandle.write('%s\n' % listitem)
    print("Sorted array is:\n")
    print(x1)
    print(x2)
    print(x3)
    print(x4)
    print(x5)
    print(x6)
    x1.reverse()  # reversed lists
    x2.reverse()
    x2.reverse()
    x3.reverse()
    x4.reverse()
    x5.reverse()
    x6.reverse()
    i_startR = int(round(time.time() * 1000))  # timer start
    insertionSort(x1)  # sort function start
    i_stopR = int(round(time.time() * 1000))  # timer stop
    suminstimeR += (i_stopR - i_startR)
    itimeR = str(i_stopR - i_startR)
    m_startR = int(round(time.time() * 1000))  # timer start
    mergeSort(x2)  # sort function start
    m_stopR = int(round(time.time() * 1000))  # timer stop
    summertimeR += (m_stopR - m_startR)
    mtimeR = str(m_stopR - m_startR)
    q1_startR = int(round(time.time() * 1000))  # timer start
    quickSort(x3, 0, n - 1)
    q1_stopR = int(round(time.time() * 1000))  # timer stop
    sumqtimeR += (q1_stopR - q1_startR)
    q1timeR = str(q1_stopR - q1_startR)
    q2_startR = int(round(time.time() * 1000))  # timer start
    quickSort_2(x4, 0, n - 1)
    q2_stopR = int(round(time.time() * 1000))  # timer stop
    sumq2timeR += (q2_stopR - q2_startR)
    q2timeR = str(q2_stopR - q2_startR)
    q3_startR = int(round(time.time() * 1000))  # timer start
    quicksort_median(x5, 0, n)
    q3_stopR = int(round(time.time() * 1000))  # timer stop
    sumq3time += (q3_stopR - q3_startR)
    q3timeR = str(q3_stopR - q3_startR)
    h_startR = int(round(time.time() * 1000))  # timer start
    heapsort(x6)
    h_stopR = int(round(time.time() * 1000))  # timer stop
    sumhtimeR += (h_stop - h_start)
    htimeR = str(h_stop - h_start)
    x = []  # these are for remove values from array because quick sort cant work without it
    x1 = []
    x2 = []
    x3 = []
    x4 = []
    x5 = []
    x6 = []
a1 = "Average of insertion sort :" + str(suminstime / 5) + "\n"
a2 = "Average of merge sort :" + str(summertime / 5) + "\n"
a3 = "Average of quick sort 1 :" + str(sumqtime / 5) + "\n1"
a4 = "Average of quick sort 2 :" + str(sumq2time / 5) + "\n"
a5 = "Average of quick sort 3 :" + str(sumq3time / 5) + "\n"
a6 = "Average of heap sort  :" + str(sumhtime / 5) + "\n"
a1r = "Average of insertion sort reversed:" + str(suminstimeR / 5) + "\n"
a2r = "Average of merge sort reversed:" + str(summertimeR / 5) + "\n"
a3r = "Average of quick sort 1 reversed:" + str(sumqtimeR / 5) + "\n1"
a4r = "Average of quick sort 2 reversed:" + str(sumq2timeR / 5) + "\n"
a5r = "Average of quick sort 3 reversed:" + str(sumq3timeR / 5) + "\n"
a6r = "Average of heap sort  reversed:" + str(sumhtimeR / 5) + "\n"
with open('statistics.txt', 'w') as filehandle:  # write statistics list into txt file
    filehandle.write(a1)
    filehandle.write(a2)
    filehandle.write(a3)
    filehandle.write(a4)
    filehandle.write(a5)
    filehandle.write(a6)
    filehandle.write(a1r)
    filehandle.write(a2r)
    filehandle.write(a3r)
    filehandle.write(a4r)
    filehandle.write(a5r)
    filehandle.write(a6r)
