from linked_list import LinkedList

class Queue:
    """
    A queue implementation using a linked list.
    
    The queue is a FIFO (First In, First Out) data structure.
    """

    def __init__(self):
        """
        Initialize a new Queue instance.
        """
        self.__queue = LinkedList()

    def enqueue(self, data):
        """
        Add an element to the rear of the queue.

        Parameters
        ----------
        data : Any
            The data to be added to the queue.
        """
        self.__queue.append(data)

    def dequeue(self):
        """
        Remove and return the front element of the queue.

        Returns
        -------
        Any or None
            The data from the front of the queue, or None if the queue is empty.
        """
        return self.__queue.pop()

    def getFront(self):
        """
        Return the front element of the queue without removing it.

        Returns
        -------
        Any or None
            The data from the front of the queue, or None if the queue is empty.
        """
        return self.__queue.getFront()

    def isEmpty(self):
        """
        Check if the queue is empty.

        Returns
        -------
        bool
            True if the queue is empty, False otherwise.
        """
        return self.__queue.size == 0

if __name__ == "__main__":
    pass