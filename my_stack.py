from linked_list import LinkedList

class Stack:
    """
    A stack implementation using a linked list.
    
    The stack is a LIFO (Last In, First Out) data structure.
    """

    def __init__(self):
        """
        Initialize a new Stack instance.
        """
        self.__stack = LinkedList()

    def push(self, data):
        """
        Add an element to the top of the stack.

        Parameters
        ----------
        data : Any
            The data to be added to the stack.
        """
        self.__stack.append(data)

    def pop(self):
        """
        Remove and return the top element of the stack.

        Returns
        -------
        Any or None
            The data from the top of the stack, or None if the stack is empty.
        """
        return self.__stack.pop()

    def peek(self):
        """
        Return the top element of the stack without removing it.

        Returns
        -------
        Any or None
            The data from the top of the stack, or None if the stack is empty.
        """
        return self.__stack.getBack()

    def isEmpty(self):
        """
        Check if the stack is empty.

        Returns
        -------
        bool
            True if the stack is empty, False otherwise.
        """
        return self.__stack.size == 0


if __name__ == "__main__":
    pass