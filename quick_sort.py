def quickSort(array: list):
    """
    Sort the data using the quick sort algorithm.
    This is the main quicksort function

    Parameters
    ----------
    array : list
        The list to sort.

    Returns
    -------
    list
        The sorted list.
    """
    quick_sort(array, 0, len(array) - 1)
    return array

def quick_sort(array: list, low: int, high: int):
    """
    Sort the data using the quick sort algorithm.
    This is the helper function for quicksort.
    
    Parameters
    ----------
    array : list
        The list to sort.
        
    low : int
        The lower index of the array.
        
    high : int
        The higher index of the array.
    """
    if low < high:
        pivot = partition(array, low, high)
        quick_sort(array, low, pivot - 1)
        quick_sort(array, pivot + 1, high)

def partition(array: list, low: int, high: int) -> int:
    """
    Partition the array and return the pivot index.
    
    Parameters
    ----------
    array : list
        The list to sort.
        
    low : int
        The lower index of the array.
        
    high : int
        The higher index of the array.
        
    Returns
    -------
    int
        The pivot index.
    """
    i = low - 1
    pivot = array[high]
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

if __name__ == "__main__":
    import sys
    array = list(map(int, sys.argv[1:][0].split(',')))
    print(quickSort(array))