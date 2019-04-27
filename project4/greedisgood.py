import random

# setting up the original list
o = [16, 51, 20, 45, 20, 2, 42, 50, 26, 16, 25, 3, 13, 14, 38, 15, 48, 32, 55, 7, 35, 46, 11, 5, 51, 56, 40, 38, 5,
     23, 5, 55, 58, 32, 6, 24, 31, 19, 56, 54, 27, 15, 1, 7, 31, 27, 58, 19, 58, 6, 7, 26, 49, 51, 42, 29, 41, 16,
     53, 24, 21, 4, 45, 4, 12, 30, 5, 41, 9, 14, 44, 30, 35, 1, 40, 20, 46, 4, 34, 25, 58, 21, 40, 59, 16, 38, 6, 8,
     50, 36, 42, 16, 26, 32, 34, 23, 29, 57, 55, 1]
# o = [] # this is for testing my algorithm
# for j in range(100):
#     num = random.randint(1, 100)
#     o.append(num)
# copy the original list for to make first biggest jobs
gmax = o.copy()
# setting processors
p1 = []
p2 = []
p3 = []
p4 = []
# sorting the list to find biggest
gmax.sort()
# assigning jobs to processors which is biggest // it was not greedy i deleted.
# for x in range(len(gmax) // 4):  # for 100/4 = 25 times
#     p1.append(gmax.pop())  # pop the last element of list gmax, add it to the processors
#     p2.append(gmax.pop())
#     p3.append(gmax.pop())
#     p4.append(gmax.pop())
while len(gmax) >= 1:
    ap = min(sum(p1), sum(p2), sum(p3), sum(p4))  # available processor which means minimum work
    if sum(p1) <= ap:  # add the next biggest value to the available processor
        p1.append(gmax.pop())
    elif sum(p2) <= ap:
        p2.append(gmax.pop())
    elif sum(p3) <= ap:
        p3.append(gmax.pop())
    elif sum(p4) <= ap:
        p4.append(gmax.pop())
# printing the total work time
print("Longest jobs first with greedy algorithm")
print("P1=", p1, "Work time =", sum(p1))
print("P2=", p2, "Work time =", sum(p2))
print("P3=", p3, "Work time =", sum(p3))
print("P4=", p4, "Work time =", sum(p4))
print("Total work time =", max(sum(p1), sum(p2), sum(p3), sum(p4)))
# shortest jobs first
gmin = o.copy()
# Sorting
gmin.sort()
# Reversing the list
gmin.reverse()
# defining new lists
p1x = []
p2x = []
p3x = []
p4x = []
for x in range(len(gmin) // 4):  # for 100/4 = 25 times
    p1x.append(gmin.pop())  # pop the last element of list gmin, add it to the processors
    p2x.append(gmin.pop())
    p3x.append(gmin.pop())
    p4x.append(gmin.pop())
# printing the total work time
print("Shortest jobs first with greedy algorithm")
print("P1=", p1x, "Work time =", sum(p1x))
print("P2=", p2x, "Work time =", sum(p2x))
print("P3=", p3x, "Work time =", sum(p3x))
print("P4=", p4x, "Work time =", sum(p4x))
print("Total work time =", max(sum(p1x), sum(p2x), sum(p3x), sum(p4x)))
# this is completely my algorithm
myAlg = o.copy()  # copy the original list
myAlg.sort()  # sort it
p1a = []  # identify the empty arrays
p2a = []
p3a = []
p4a = []
while len(myAlg) >= 1:
    p1a.append(myAlg.pop())  # biggest number into processor 1
    maxi = sum(p1a)  # processor 1 is always maximum array
    while sum(myAlg) >= 1 and sum(p2a) < maxi:  # if there is an element in the list and p2 lower than max
        if sum(p2a) + myAlg[-1] < maxi:  # if the summation of last element and p2 will be lower than max
            p2a.append(myAlg.pop())  # add this last element into p2
        else:
            break
    while sum(myAlg) >= 1 and sum(p3a) < maxi:  # same as p2
        if sum(p3a) + myAlg[-1] < maxi:
            p3a.append(myAlg.pop())
        else:
            break
    while sum(myAlg) >= 1 and sum(p4a) < maxi:  # same as p2
        if sum(p4a) + myAlg[-1] < maxi:
            p4a.append(myAlg.pop())
        else:
            break
mini = min(p1a, p2a, p3a, p4a)  # find minimum work on array
mini.append(p1a.pop())  # take the last value of p1 and add it to the minimum array
# printing the total work time
print("My algorithm")
print("P1=", p1a, "Work time =", sum(p1a))
print("P2=", p2a, "Work time =", sum(p2a))
print("P3=", p3a, "Work time =", sum(p3a))
print("P4=", p4a, "Work time =", sum(p4a))
print("Total work time =", max(sum(p1a), sum(p2a), sum(p3a), sum(p4a)))
