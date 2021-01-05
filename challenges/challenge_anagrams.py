def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp
    
def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
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

def sort(array):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array
def is_anagram_selectionSort(first_string, second_string):
    if len(first_string) != len(list(second_string)):
        return False

    first_sorted = selectionSort(list(first_string))
    second_sorted = selectionSort(list(second_string))

    return first_sorted == second_sorted

def is_anagram_insertionSort(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    first_sorted = insertionSort(list(first_string))
    second_sorted = insertionSort(list(second_string))

    return first_sorted == second_sorted

def is_anagram_bubbleSort(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    first_sorted = bubbleSort(list(first_string))
    second_sorted = bubbleSort(list(second_string))

    return first_sorted == second_sorted

def is_anagram_mergeSort(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    first_sorted = mergeSort(list(first_string))
    second_sorted = mergeSort(list(second_string))

    return first_sorted == second_sorted

def is_anagram_quickSort(first_string, second_string):
    if len(first_string) != len(list(second_string)):
        return False

    first_sorted = quickSort(list(first_string))
    second_sorted = quickSort(list(second_string))

    return first_sorted == second_sorted

def is_anagram_sort(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    first_sorted = sort(list(first_string))
    second_sorted = sort(list(second_string))

    return first_sorted == second_sorted