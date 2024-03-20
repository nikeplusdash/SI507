# you may use pandas only for IO reason
# Using it to do sort will impact your grade
import pandas as pd
import random
import timeit
import codecs

def timeFunc(method):
    """
    Define the main body of the decorator that decorates a method.
        
    Returns
    -------
    Callable
        A wrapper that defines the behavior of the decorated method
    """
    def wrapper(*args, **kwargs):
        """
        Define the behavior of the decorated method
        Parameters:
            Same as the parameters used in the methods to be decorated
            
        Returns:
            Same as the objects returned by the methods to be decorated
        """
        start = timeit.default_timer()
        result = method(*args, **kwargs)  
        # record the time consumption of executing the method
        time = timeit.default_timer() - start
        
        # send metadata to standard output
        print(f"Method: {method.__name__}")
        print(f"Result: {result}")
        print(f"Elapsed time of 10000 times: {time*10000} seconds")
        return result
    return wrapper


class MusicLibrary:
    def __init__(self):
        """
        Initialize the MusicLibrary object with default values.
        self.data the collect of music library
        self.rows: the row number 
        self.cols: the col number 
        self.nameIndex: the number represent the index of name in each element of self.data
        self.albumIndex: the number represent the index of album in each element of self.data
        self.trackIndex: the number represent the index of track in each element of self.data
        """
        self.data = []
        self.rows = 0
        self.cols = 0
        self.nameIndex = 0
        self.albumIndex = 1
        self.trackIndex = 1

    def readFile(self, fileName):
        """
        Read music data from a CSV file and store it in the self.data attribute.
        The self.rows and self.cols should be updated accordingly. 
        The item in self.data should be [name, albums count, tract count]
        You could assume the file is in the same directory with your code

        Parameters
        ----------
        fileName : str
            The file name of the CSV file to be read.
        """
        # df = pd.read_csv(fileName, engine='python')
        with codecs.open(fileName, 'r', encoding='utf-8',errors='ignore') as fdata:
            self.data = [line.strip().split(',') for line in fdata]
        self.rows = len(self.data)
        self.cols = len(self.data[0])


    def printData(self):
        """
        Print the data attribute stored in the library instance in a formatted manner.
        """
        for row in self.data:
            print(f"Name: {row[0]}, Albums Count: {row[1]}, Tract Count: {row[2]}")           

    def shuffleData(self):
        """
        Shuffle the data stored in the library.
        refer to the random package
        """
        random.shuffle(self.data)

    @timeFunc
    def binarySearch(self, key, keyIndex):
        """
        Perform a binary search on the data.

        Parameters
        ----------
        key : int or str
            The key to search for.
        keyIndex : int
            The column index to search in.

        Returns
        -------
        int
            The index of the row where the key is found, or -1 if not found.
        """
        left = 0
        right = self.rows - 1
        while left <= right:
            mid = (left + right) // 2
            if self.data[mid][keyIndex] == key:
                return mid
            elif self.data[mid][keyIndex] < key:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    @timeFunc
    def seqSearch(self, key, keyIndex):
        """
        Perform a sequential search on the data.

        Parameters
        ----------
        key : int or str
            The key to search for.
        keyIndex : int
            The column index to search in.

        Returns
        -------
        int
            The index of the row where the key is found, or -1 if not found.
        """
        for i in range(self.rows):
            if self.data[i][keyIndex] == key:
                return i
        return -1

    @timeFunc
    def bubbleSort(self, keyIndex):
        """
        Sort the data using the bubble sort algorithm based on a specific column index.
        self.data will have to be in sorted order after calling this function.

        Parameters
        ----------
        keyIndex : int
            The column index to sort by.
        """
        for i in range(self.rows):
            for j in range(self.rows - i - 1):
                if self.data[j][keyIndex] > self.data[j + 1][keyIndex]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]

    def merge(self, L, R, keyIndex):
        """
        Merge two sorted sublists into a single sorted list.
        This is the helper function for merge sort.
        You may change the name of this function or even not have it.
        

        Parameters
        ----------
        L, R : list
            The left and right sublists to merge.
        keyIndex : int
            The column index to sort by.

        Returns
        -------
        list
            The merged and sorted list.
        """
        # Implementation details...
        pass

    @timeFunc
    def mergeSort(self, keyIndex):
        """
        Sort the data using the merge sort algorithm.
        This is the main mergeSort function

        Parameters
        ----------
        keyIndex : int
            The column index to sort by.
        """
        pass

    def _mergeSort(self, arr, keyIndex):

        # This is the helper function for merge sort.
        # You may change the name of this function or even not have it.
        # This is a helper method for mergeSort
        pass

    @timeFunc
    def quickSort(self, keyIndex):
        """
        Sort the data using the quick sort algorithm.
        This is the main quickSort function

        Parameters
        ----------
        keyIndex : int
            The column index to sort by.
        """
        # Implementation details...
        pass

    def _quickSort(self, arr, keyIndex):
        # This is a helper method for quickSort
        # ...
        pass

    def comment(self):
        '''
        Based on the result you find about the run time of calling different function,
        Write a small paragraph (more than 50 words) about time complexity, and print it. 
        '''
        # print(you comment)
        pass



# create instance and call the following instance method
# using decroator to decroate each instance method
def main():
    random.seed(42)
    myLibrary = MusicLibrary()
    filePath = 'music.csv'
    myLibrary.readFile(filePath)

    idx = 0
    myLibrary.data.sort(key = lambda data: data[idx])
    myLibrary.seqSearch(key="30 Seconds To Mars", keyIndex=idx)
    myLibrary.binarySearch(key="30 Seconds To Mars", keyIndex=idx)

    idx = 2
    myLibrary.shuffleData()
    myLibrary.bubbleSort(keyIndex=idx)
    # myLibrary.shuffleData()
    # myLibrary.quickSort(keyIndex=idx)
    # myLibrary.shuffleData()
    # myLibrary.mergeSort(keyIndex=idx)
    # myLibrary.printData()

if __name__ == "__main__":
    main()

