
import time
import timeit
import numpy as np
import random
import csv
import math

"""Global Variables"""
loader = "....."
spacer = "-=--=-=-=-=-=-=-=-=-="
REPEATS = 3           #No times to run sorts to get mean time
NEARLY_PERCENT = 0.10 #% of items to move in nearly sorted array
RANDOM_TIMES = 100    #No times to randomly swap elements in array


class DSA_Sorts():

    """Constructor"""
    def __init__(self, array):

        self.array = array
        self.size = len(self.array)
    
    def bubbleSort(self, A):
        """Bubble Sort Algorithm"""

        index_length = self.size - 1 #determining the length of given list

        sorted = False # setting variable sorted to False

        while not sorted: # meaning while Sorted = True

            sorted = True 

            for ii in range(0, index_length): # loop to make each index(ii) in list addressable
                if self.array[ii] > self.array[ii+1]: # if current index value is greater than next index value
                    sorted = False # if above line is true, sorted = False
                    self.array[ii], self.array[ii+1] = self.array[ii+1], self.array[ii] # if above lines are True, reformat list

        return self.array # return sorted list
 

    def insertionSort(self, A):
        """Insertion Sort Algorithm"""

        self.array = A

        indexing_length = self.size #determining the length of given list

        for ii in range(0, indexing_length): # making each element in given list addressable

            value_to_sort = self.array[ii] #declaring current interation as value to be sorted

            while self.array[ii-1] > value_to_sort and ii > 0: #meaning 2,1 would become 1,2

                self.array[ii], self.array[ii-1] = self.array[ii-1], self.array[ii] # reformats list

                ii -= 1 # then the switch takes the lists length down by 1 

        return self.array # returns sorted list


    def selectionSort(self, A):
        """Selection Sort Algorithm"""

        self.array = A

        indexing_length = range(self.size) #determing the length of the given list

        for ii in indexing_length:

            print(ii)

            min_value = ii 

            for jj in range(ii+1, self.size): #looping through list in range min value + 1 to size list

                if self.array[min_value] > self.array[jj]: # if current index value is less than min value

                    min_value = jj # this current index value is now set as min value 

            self.array[ii], self.array[min_value] = self.array[min_value], self.array[ii]

        return self.array
    
    def mergeSort(self):
        """Merge Sort Algorithm"""

        if len(self.array) > 1:
            m = len(self.array)//2
            left = self.array[:m]
            right = self.array[m:]

            leftsorter = DSA_Sorts(left)
            leftsorter.mergeSort()
            rightsorter = DSA_Sorts(right)
            rightsorter.mergeSort()

            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    self.array[k] = left[i]
                    i += 1
                else:
                    self.array[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                self.array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                self.array[k] = right[j]
                j += 1
                k += 1


    """Quick Sorts Seciton"""
    """3 Way QuickSort Start Block"""
    def three_swap(self, A, index, jindex):
        """Swaps index for 3 way Quick Sort"""

        self.array = A

        temp = self.array[index]
        self.array[index] = self.array[jindex]
        self.array[jindex] = temp

    def dnf_a(self, A, start, end):
        """partitioning routine using the dutch national flag algrothim"""

        self.array = A

        median = start
        piv = self.array[end]


        while median <= end:

            if self.array[median] < piv:
                self.three_swap(self.array, start, median)
                start += 1
                median += 1

            elif self.array[median] > piv:
                self.three_swap(self.array, median, end)
                end -= 1
            
            else:
                median += 1
        
        return start - 1, median


    def three_way_quicksort(self, A, start, end):
        """Implementation of 3 way Quick Sort"""

        self.array = A

        if start >= end:
            return
        
        if start - end == 1:
            if self.array[start] < self.array[end]:
                self.three_swap(self.array, start, end)
            return

        row, col = self.dnf_a(self.array, start, end)

        self.three_way_quicksort(self.array, start, row)

        self.three_way_quicksort(self.array, col, end)

    """3 Way QuickSort end block"""


    """Median QuickSort Start Block"""

    def median_quicksort(self):

        self.recursive_quicksort(0, self.size -1)

    def recursive_quicksort(self, left, right):

        length = right - left + 1

        if length <= 3:
            self.manual_sort(left, right)
        else:
            median = self.median_of_three(left, right)
            part = self.median_partition(left, right, median)
            self.recursive_quicksort(left, part-1)
            self.recursive_quicksort(part+1, right)
    
    def median_of_three(self, left, right):

        middle = int((left + right)/2)

        if self.array[left] > self.array[middle]:
            self.median_swap(left, middle)
        if self.array[left] > self.array[right]:
            self.median_swap(left, right)
        if self.array[middle] > self.array[right]:
            self.median_swap(middle, right)
        
        self.median_swap(middle, right -1)

        return self.array[right -1]
    
    def median_swap(self, index, jindex):

        self.array[index], self.array[jindex] = self.array[jindex], self.array[index]
    
    def median_partition(self, left, right, piv):

        left_mark = left
        right_mark = right -1

        while True:
            left_mark += 1

            while self.array[left_mark] < piv:
                left_mark += 1
            
            right_mark -= 1

            while self.array[right_mark] > piv:
                right_mark -= 1
            
            if left_mark >= right_mark:
                break
            else:
                self.median_swap(left_mark, right_mark)
        
        self.median_swap(left_mark, right -1)
        return left_mark
    
    def manual_sort(self, left, right):

        length = right - left + 1

        if length <= 1:
            return
        if length == 2:
            if self.array[left] > self.array[right]:
                self.median_swap(left, right)
            return
        
        else:
            if self.array[left] > self.array[right -1]:
                self.median_swap(left, right-1)
            
            if self.array[left] > self.array[right]:
                self.median_swap(left, right)
            
            if self.array[right -1] > self.array[right]:
                self.median_swap(right-1, right)
        

    """Median QuickSort end block"""


    """ Native QuickSort Start Block"""

    def quick_sort(self, A, start, end):
        """quick sort sorting algorithm"""
        """ BC: 0(n log(n)) """
        """ WC: 0(n^2) """

        self.array = A

        if start < end:
            piv = self.native_partition(self.array, start, end)
            self.quick_sort(self.array, start, piv-1)
            self.quick_sort(self.array, piv+1, end)

    
    def native_partition(self, A, start, end):

        xx = self.array[end]
        ii = start - 1

        for jj in range(start, end+1, 1):

            if self.array[jj] <= xx:
                ii += 1

                if ii < jj:
                    zz = self.array[ii]
                    self.array[ii] = self.array[jj]
                    self.array[jj] = zz
        
        return ii 

    """Native QuickSort End Block"""



    def menu(self):
        """menu to terminal function"""

        print(spacer)
        print("        num =  is number of integers to sort")
        print("        Type corresponding letter for desired sorting algorithm")
        print("           b - bubblesort")
        print("           i - insertion sort")
        print("           s - selection sort")
        print("           q1 - quicksort native")
        print("           q2 - quicksort 3 way")
        print("           q3   quicksort median of 3")
        print("           m - mergesort")
        print(" ")
        print("           all q - All QuickSorts")
        print(" ")
        print("        Type corresponding letter for desired order")
        print("           a - 1..n ascending")
        print("           d - 1..n descending")
        print("           r - 1..n in random order")
        print("           n - 1..n nearly sorted (10% moved)")
        print(spacer)

    def user_inp(self):
        """gets Users Selecitons"""

        self.size = int(input("Enter Desired Number Of Integers To Sort:  "))
        self.sort_selection = str(input("Enter Letter For Sorting Algorithm Selection:  "))
        self.array_type = str(input("Enter Letter For Array Type Selection:  "))


    def order(self):

        if self.array_type == 'a': # outputs sorted array as default

            for i in range(0, int(self.size)):
                temp = self.array[i]
                self.array[i] = temp

            print("Ascending: ", self.array)

        elif self.array_type == 'd':  #convert to descending

            for i in range(0, int(self.size/2)):
                temp = self.array[i]
                self.array[i] = self.array[self.size-i-1]
                self.array[self.size-i-1] = temp

            print("Descending: ", self.array)

        elif self.array_type == 'r':

            for i in range(RANDOM_TIMES*self.size):
                x = int(random.random()*self.size)
                y = int(random.random()*self.size)
                temp = self.array[x]
                self.array[x] = self.array[y]
                self.array[y] = temp

            print("Random: ", self.array)

        elif self.array_type == 'n':

            for i in range(int(self.size*NEARLY_PERCENT/2+1)):
                x = int(random.random()*self.size)
                y = int(random.random()*self.size)
                temp = self.array[x]
                self.array[x] = self.array[y]
                self.array[y] = temp

            print("Nearly sorted: ", self.array)

        else:

            print("Unsupported array type")

    def sort_type(self):
        """Selects User Given Sorting Type"""

        for val in range(1, self.size + 1):
            val = np.random.randint(0, 100)
            self.array.append(val)

        if self.sort_selection == "b":
            print(loader)
            print("Bubble Sort")
            print("Initial Array:  ", self.array)
            start_time = timeit.default_timer()
            self.bubbleSort(self.array)
            print(loader)
            self.order()
            end_time = timeit.default_timer()
            run_time = end_time - start_time
            run_time = float(round(run_time, 4))
            print("Run Time:  ", run_time)


        elif self.sort_selection == "s":
            print(loader)
            print("Selection Sort")
            print("Initial Array:  ", self.array)
            start_time = timeit.default_timer()
            self.selectionSort(self.array)
            print(loader)
            self.order()
            end_time = timeit.default_timer()
            run_time = end_time - start_time
            run_time = float(round(run_time, 4))
            print("Run Time:  ", run_time)


        elif self.sort_selection == "i":
            print(loader)
            print("Insertion Sort")
            print("Initial Array:  ", self.array)
            start_time = timeit.default_timer()
            self.insertionSort(self.array)
            print(loader)
            self.order()
            end_time = timeit.default_timer()
            run_time = end_time - start_time
            run_time = float(round(run_time, 4))
            print("Run Time:  ", run_time)


        elif self.sort_selection == "m":
            print(loader)
            print("Merge Sort")
            print("Initial Array:  ", self.array)
            start_time = timeit.default_timer()
            self.mergeSort()
            print(loader)
            self.order()
            end_time = timeit.default_timer()
            run_time = end_time - start_time
            run_time = float(round(run_time, 4))
            print("Run Time:  ", run_time)


        elif self.sort_selection == "q1":
            print(loader)
            print("Native QuickSort")
            print("Initial Array:  ", self.array)
            start_time = timeit.default_timer()
            self.quick_sort(self.array, 0, self.size - 1)
            print(loader)
            self.order()
            end_time = timeit.default_timer()
            run_time = end_time - start_time
            run_time = float(round(run_time, 4))
            print("Run Time:  ", run_time)

        
        elif self.sort_selection == "q2":
            print(loader)
            print("3 Way QuickSort")
            print("Initial Array:  ", self.array)
            start_time = timeit.default_timer()
            self.three_way_quicksort(self.array, 0, self.size - 1)
            print(loader)
            self.order()
            end_time = timeit.default_timer()
            run_time = end_time - start_time
            run_time = float(round(run_time, 4))
            print("Run Time:  ", run_time)

        
        elif self.sort_selection == "q3":
            print(loader)
            print("Median QuickSort")
            print("Initial Array:  ", self.array)
            start_time = timeit.default_timer()
            self.median_quicksort()
            print(loader)
            self.order()
            end_time = timeit.default_timer()
            run_time = end_time - start_time
            run_time = float(round(run_time, 4))
            print("Run Time:  ", run_time)
        
        elif self.sort_selection == "all q":

            running_list = []

            print(loader)
            print("Native QuickSort")
            print("Initial Array:  ", self.array)
            start_time = timeit.default_timer()
            self.quick_sort(self.array, 0, self.size - 1)
            print(loader)
            self.order()
            end_time = timeit.default_timer()
            run_time = end_time - start_time
            run_time = float(round(run_time, 5))
            running_list.append(run_time)
            print("Run Time:  ", run_time)

            
            print(loader)
            print(spacer)
            print(loader)

            print("3 Way QuickSort")
            print("Initial Array:  ", self.array)
            start_time = timeit.default_timer()
            self.three_way_quicksort(self.array, 0, self.size - 1)
            print(loader)
            self.order()
            end_time = timeit.default_timer()
            run_time = end_time - start_time
            run_time = float(round(run_time, 5))
            running_list.append(run_time)
            print("Run Time:  ", run_time)

            print(loader)
            print(spacer)
            print(loader)

            print("Median QuickSort")
            print("Initial Array:  ", self.array)
            start_time = timeit.default_timer()
            self.median_quicksort()
            print(loader)
            self.order()
            end_time = timeit.default_timer()
            run_time = end_time - start_time
            run_time = float(round(run_time, 5))
            running_list.append(run_time)
            print("Run Time:  ", run_time)

            print(spacer)

            print("Native Quicksort RunTime:  ", running_list[0])
            print("3 Way QuickSort RunTime:  ", running_list[1])
            print("Median Quicksort RunTime: ", running_list[2])

            print(loader)
            print(loader)

            quickest = min(running_list)

            if quickest == running_list[0]:
                quickest_a = "Native QuickSort"
            elif quickest == running_list[1]:
                quickest_a = "3 Way QuickSort"
            else:
                quickest_a = "Median QuickSort"


            print("Quickest Algorithm:  ", quickest_a, " " + "With RunTime: ", quickest)

        else:
            print("Unsupported sort algorithm")
            pass


"""Test Harness"""
if __name__ == "__main__":

    sorter = DSA_Sorts([])

    sorter.menu()
    sorter.user_inp()
    sorter.sort_type()












