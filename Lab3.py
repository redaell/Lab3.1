print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1


def bubble_sort(arr, sorting_order):
 
    # Copy input list to results list
    arr_result = arr.copy()

    # Get number of elements in the list
    n = len(arr_result)

<<<<<<< HEAD
    if n==0:
        return 0
    if n>= 10:
        return 1
    
    for item in arr_result:
        if isinstance(item, int)==False:
            return 2
    

=======
    if n == 0:
        return 0
    if n >= 10:
        return 1
    
    for item in arr_result:
        if isinstance(item, int)==False: #check if the instance of the object is an integer. if not, return 2
            return 2
>>>>>>> df7c82d0eeaf159650082eda5acd96ee5cba3f6b

    if n < 10:
        # Traverse through all array elements
        for i in range(n - 1):
            # range(n) also work but outer loop will
            # repeat one time more than needed.

            # Last i elements are already in place
            for j in range(0, n - i - 1):

                if sorting_order == SORT_ASCENDING:
                    if arr_result[j] > arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]


                elif sorting_order == SORT_DESCENDING:
                    if arr_result[j] < arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

                else:
                    # Return an empty array
                    arr_result = []
    else:
        arr_result = -1

    return arr_result

def main():
    # Driver code to test above
    arr = [64, 34, 25, 12, 22, 11, 90]

    # Sort in ascending order
    result = bubble_sort(arr, SORT_ASCENDING)
    print("\nSorted array in ascending order: ")
    print(result)

    # Sort in descending order
    print("Sorted array in descending order: ")
    result = bubble_sort(arr, SORT_DESCENDING)
    print(result)

    # Testing of zero array
    print("Sort an empty list: ")
    empty_arr = []
    result = bubble_sort(empty_arr, SORT_DESCENDING)
    print(result)

    print("Sort a too-long list ")
    long_arr = [64, 34, 25, 12, 22, 11, 90, 5, 7, 23]
    result = bubble_sort(long_arr, SORT_DESCENDING)
    print(result)

    print("Sort a non-integer list: ")
    non_int_arr = [64, 34, 25, 12, 22, 11.1, 90]
    result = bubble_sort(non_int_arr, SORT_DESCENDING)
    print(result)

if __name__ == "__main__":
    main()


