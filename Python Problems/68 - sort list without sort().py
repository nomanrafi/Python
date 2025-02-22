# Write a program that can sort a given unsorted list.
# Don't use any built-in function for sorting.
L = [5, 2, 3, 6, 4, 7]

for i in range(len(L)):
    for k in range(0, len(L)-1):
        if L[k] > L[k+1]:
            