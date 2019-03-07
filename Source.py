# import random
#
# x = []
# for j in range(0, 10000):
#     num = random.randint(1, 2000000)
#     x.append(num)
# with open('originalList5.txt', 'w') as filehandle:
#     for listitem in x:
#         filehandle.write('%s\n' % listitem)
import time
# test=[]
# with open('sortedList.txt', 'r') as filehandle:
#     for line in range(0,3):
#         currentPlace = int(line[:-1])
#         test.append(currentPlace)
# print(y)
x = []
with open('originalList5.txt', 'r') as filehandle:
    for line in filehandle:
        currentPlace = int(line[:-1])
        x.append(currentPlace)


def insertionSort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while (i > -1) and key < array[i]:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key
    return array


def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        # recursion
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i = i + 1
            else:
                array[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            array[k] = righthalf[j]
            j = j + 1
            k = k + 1


start = time.time()
# insertionSort(x)
x.sort()
# mergeSort(x)
stop = time.time()
print(x)
print(stop - start)
# with open('sortedList5.txt', 'w') as filehandle:
#     for listitem in x:
#         filehandle.write('%s\n' % listitem)


avgInsertionSort = (
                           6.108926773071289 + 6.030807256698608 + 6.008946084976196 + 6.280808687210083 + 6.062066555023193 + 5.9839372634887695 + 6.030825138092041 + 6.108946084976196 + 6.108946084976456 + 6.171425104141235 + 5.999558448791504 + 5.95268702507019 + 6.04643440246582 + 6.093322038650513 + 6.093322038650513 + 6.1870269775390625 + 6.171424865722656 + 6.030824899673462 + 5.968331575393677 + 6.202671766281128 + 5.937065362930298 + 5.968331575393677 + 5.921440839767456 + 6.030808925628662 + 6.1558146476745605) / 25
avgMergeSort = (
                       0.10936880111694336 + 0.06251120567321777 + 0.07811641693115234 + 0.07811737060546875 + 0.06249284744262695 + 0.07810831069946289 + 0.07812070846557617 + 0.07812047004699707 + 0.07811999320983887 + 0.07811808586120605 + 0.07811856269836426 + 0.07121856269436213 + 0.07811808586120605 + 0.066491655349731785 + 0.07811713218688965 + 0.07811784744262695 + 0.07811665534973145 + 0.07811713218688965 + 0.062491655349731445 + 0.07812023162841797 + 0.07811975479125977 + 0.07811808586120605 + 0.07811951637268066 + 0.07813429832458496 + 0.07811808586120605) / 25
avgTimSort = (
                     0.015623092651367188 + 0.0 + 0.015624523162841797 + 0.0 + 0.0 + 0.015622377395629883 + 0.0 + 0.015624761581420898 + 0.0 + 0.015624046325683594 + 0.0 + 0.0 + 0.01262951215300093 + 0.0 + 0.0 + 0.0 + 0.0 + 0.015619754791259766 + 0.0 + 0.015622854232788086 + 0.015624523162841797 + 0.0 + 0.01562952995300293 + 0.0 + 0.015623807907104492) / 25
print(avgInsertionSort, avgMergeSort, avgTimSort)
