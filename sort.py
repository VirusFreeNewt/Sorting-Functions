# Miscellaneous sorting functions
# Based on code created by Joe Marini from Lynda.com
# Created 5/28/2019 By: Ethan Goodwin

# Learn about algorithms here:
# https://www.lynda.com/Software-Development-tutorials/Programming-Foundations-Algorithms/718636-2.html


# Mostly used for demonstrative purposes, has quadratic time
# O(n^2) n = number of values
def bubblesort(data):

    for i in range(len(data)-1, 0, -1):  # for each value in the dataset
        # this sets a value (i) to the current range of the dataset
        for j in range(i):  # for each value that needs to be sorted
            if data[j] > data[j+1]:  # check if a value is greater than another
                # swap a value in the dataset with the next one
                temp = data[j]  # temporary variable to store data[j]
                data[j] = data[j+1]
                data[j+1] = temp


# Is a good method of sorting, but usually isn't the best
# Has loglinear time
def mergesort(dataset):

    # if the dataset is greater than one, set the midpoint to the middle
    # splice the dataset array from the left and right of the midpoint
    if len(dataset) > 1:
        midpoint = len(dataset) // 2
        left_array = dataset[:midpoint]
        right_array = dataset[midpoint:]

        # recursively preform the splitting until there is only one
        # individual value in each array
        mergesort(left_array)
        mergesort(right_array)

        # indices of the left, right, and merged arrays
        left_index = 0
        right_index = 0
        merged_index = 0

        # while both Arrays contain elements
        while left_index < len(left_array) and right_index < len(right_array):

            # if the left array is less than the right
            # then set the left array as the set index from the merged array
            if left_array[left_index] < right_array[right_index]:
                dataset[merged_index] = left_array[left_index]
                left_index += 1
            # otherwise, do this to the right
            else:
                dataset[merged_index] = right_array[right_index]
                right_index += 1
            merged_index += 1

        # if the left array still contains values, add them
        while left_index < len(left_array):

            dataset[merged_index] = left_array[left_index]
            left_index += 1
            merged_index += 1

        while right_index < len(right_array):

            dataset[merged_index] = right_array[right_index]
            right_index += 1
            merged_index += 1


# On average really good and usually has quasilinear time
# In the worst case, it has quadratic time
# Pivot: the value that things will be sorted based on
def quicksort(dataset, first, last):  # first is the starting value and is the pivot point

    # Divides the halves and returns the new pivot point
    # This is used by the quicksort function
    def partition(datavalues, first, last):

        # chose our first value in the dataset as the pivot point
        pivot_value = datavalues[first]

        lower_index = first + 1  # lower index to be checked is the value after the pivot
        upper_index = last  # higher index to be checked is the last value

        # start searching for the crossing point
        # this is when the upper_index has an index value less than the lower_index
        # example: upper_index = 2 & lower_index = 3
        while True:

            # move the lower index up one if it is less than the upper index
            # example: lower_index = 2 and upper_index = 3
            # and if the element of the lower_index is less than the pivot_value
            while lower_index <= upper_index and datavalues[lower_index] <= pivot_value:
                lower_index += 1

            # move the upper index down one if it is greater than the lower index
            # and if the element of the upper index is greater than the pivot value
            while upper_index >= lower_index and datavalues[upper_index] >= pivot_value:
                upper_index -= 1

            # if the indices have crossed, then break
            # (upper index is less than lower index)
            # example: upper index = 2 and lower index = 3
            if upper_index < lower_index:
                break
            # otherwise swap the elements of the upper and lower values
            else:
                temp = datavalues[lower_index]  # temporary variable to store the lower index
                datavalues[lower_index] = datavalues[upper_index]
                datavalues[upper_index] = temp

        # when two indices have crossed, exchange the pivot value
        # with upper_index (which is now actually a lower index value than lower_index)
        temp = datavalues[first]  # temporary variable the store datavalues[first] in
        datavalues[first] = datavalues[upper_index]
        datavalues[upper_index] = temp

        # return the new pivot's index
        return upper_index

    if first < last:

        # calculate the new pivot
        pivot_index = partition(dataset, first, last)

        # ethan the two partitions
        quicksort(dataset, first, pivot_index - 1)
        quicksort(dataset, pivot_index + 1, last)
