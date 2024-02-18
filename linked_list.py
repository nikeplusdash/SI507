class Node:
    """
    A node in a doubly linked list.

    Attributes
    ----------
    data : Any
        The data stored in the node.
    next : Node or None
        The next node in the linked list.
    prev : Node or None
        The previous node in the linked list.

    Parameters
    ----------
    data : Any, optional
        The data to be stored in the node (default is None).
    """
    
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    """
    A doubly linked list with dummy head and tail nodes to simplify node insertion and deletion.
    We require using dummyHead and dummyTail, since it will make certain implementation easier.
    Notice, the linked list is zero indexed.  

    Attributes
    ----------
    dummyHead : Node
        A dummy head node of the linked list.
    dummyTail : Node
        A dummy tail node of the linked list.
    size : int
        The number of elements in the linked list.

    Methods
    -------
    get(index)
        Retrieves the data at the specified index in the linked list.

    getNode(index)
        Retrieves the node at the specified index.

    appendLeft(data)
        Adds a node with the given data at the beginning of the linked list.

    append(data)
        Adds a node with the given data at the end of the linked list.

    popLeft()
        Removes and returns the data from the beginning of the linked list.

    pop()
        Removes and returns the data from the end of the linked list.

    addAtIndex(index, data)
        Adds a node with the given data at the specified index in the linked list.

    deleteAtIndex(index)
        Deletes the node at the specified index from the linked list.

    printFromFront()
        Prints all elements of the linked list from front to back.

    printFromBack()
        Prints all elements of the linked list from back to front.

    _isNodeUnbound(node)
        Checks if the given node's linkage in the list is broken. 
        More specifically, check if the node is removed.

    getFront()
        Returns the data from the front (head) of the linked list.

    getBack()
        Returns the data from the back (tail) of the linked list.

    getSize()
        Returns the number of elements in the linked list.
    """

    def __init__(self):
        """
        Initializes a LinkedList instance with dummy head and tail nodes and sets size to zero.
        Notice data attribute of the dummyHead and dummyTail is None
        """
        self.dummyHead = Node(None)
        self.dummyTail = Node(None)
        self.dummyHead.next = self.dummyTail
        self.dummyTail.prev = self.dummyHead
        self.size = 0
    
    def get(self ,index: int) -> int:
        """
        Retrieve the data at the specified index in the linked list.
        If the index is invalid, ie out of range, return None.


        Parameters
        ----------
        index : int
            The index of the node whose data is to be retrieved.

        Returns
        -------
        any or None
            The data at the specified index or None if index is invalid.
        """
        return self.getNode(index).data
        
    def getNode(self, index: int) -> Node:
        """
        Retrieve the node at the specified index in the linked list.
        If the index is invalid, ie out of range, return None.

        Parameters
        ----------
        index : int
            The index of the node to be retrieved.

        Returns
        -------
        Node or None
            The node at the specified index or None if index is invalid.
        """
        if index < 0 or index >= self.size:
            return None
        else:
            current = self.dummyHead.next
            for _ in range(index):
                current = current.next
            return current


    def appendLeft(self, data):
        """
        Create a new node, and assign the data to the new node.
        Add the node with the given data at the beginning of the linked list.
        Reset the positional relation(the next and prev attribute) of three
        related nodes.
        Increment the size by one.

        Parameters
        ----------
        data : any
            The data to be stored in the new node.

        Returns
        -------
        None
        """
        newNode = Node(data)
        if self.size == 0:
            self.dummyHead.next = newNode
            newNode.prev = self.dummyHead
            newNode.next = self.dummyTail
            self.dummyTail.prev = newNode
        else:
            newNode.next = self.dummyHead.next
            self.dummyHead.next.prev = newNode
            newNode.prev = self.dummyHead
            self.dummyHead.next = newNode
        self.size += 1

    def append(self, data):
        """
        Add a node with the given data at the end of the linked list.
        Reset the positional relation(the next and prev attribute) of three
        related nodes.
        Increment the size by one.

        Parameters
        ----------
        data : any
            The data to be stored in the new node.

        Returns
        -------
        None
        """
        newNode = Node(data)
        if self.size == 0:
            self.dummyHead.next = newNode
            newNode.prev = self.dummyHead
            newNode.next = self.dummyTail
            self.dummyTail.prev = newNode
        else:
            newNode.prev = self.dummyTail.prev
            self.dummyTail.prev.next = newNode
            newNode.next = self.dummyTail
            self.dummyTail.prev = newNode
        self.size += 1

    
    def popLeft(self):
        """
        Remove and return the data from the beginning of the linked list.
        Decrease the size by one.
        Reset the positional relation(the next and prev attribute) of three
        related nodes.

        Returns
        -------
        any
            The data of the removed node, or None if the list is empty.

        None 
            If the linked list is empty.
        """
        if self.size == 0:
            return None
        else:
            delNode = self.dummyHead.next
            data = delNode.data
            self.dummyHead.next = delNode.next
            delNode.next.prev = self.dummyHead
            delNode = None
            self.size -= 1
            return data 


    def pop(self):
        """
        Remove and return the data from the end of the linked list.
        Decrease the size by one.
        Reset the positional relation(the next and prev attribute) of three
        related nodes.

        Returns
        -------
        any
            The data of the removed node, or None if the list is empty.
        None 
            If the linked list is empty.
        """
        if self.size == 0:
            return None
        else:
            delNode = self.dummyTail.prev
            data = delNode.data
            self.dummyTail.prev = delNode.prev
            delNode.prev.next = self.dummyTail
            delNode = None
            self.size -= 1
            return data
            

    def addAtIndex(self, index: int, data: int):
        """
        Add a node with the given data at the specified index in the linked list.
        You could assume the only illegal input is an out of range index. 
        Notice, you need to reset the connection at both side. 

        Parameters
        ----------
        index : int
            The index at which the new node should be inserted.
        data : any
            The data to be stored in the new node.

        Returns
        -------
        bool
            True if the addition was successful, False otherwise.
        """
        if index < 0 or index > self.size:
            return False
        else:
            newNode = Node(data)
            current = self.dummyHead
            for _ in range(index):
                current = current.next
            newNode.next = current.next
            current.next.prev = newNode
            newNode.prev = current
            current.next = newNode
            self.size += 1
            return True


    def deleteAtIndex(self, index: int):
        """
        Delete a node with the given data at the specified index in the linked list.
        You could assume the only illegal input is an out of range index. 
        Notice, you need to reset the connection at both side. 

        Parameters
        ----------
        index : int
            The index at which the new node should be inserted.
        data : any
            The data to be stored in the new node.

        Returns
        -------
        bool
            True if the addition was successful, False otherwise.
        """
        if index < 0 or index >= self.size:
            return False
        else:
            current = self.dummyHead
            for _ in range(index):
                current = current.next
            delNode = current.next
            current.next = delNode.next
            delNode.next.prev = current
            delNode = None
            self.size -= 1
            return True


    def printFromFront(self):
        """
        Print all elements of the linked list from front to back,
        each element should be in a separate line. 
        If the linked list is empty, print exactly this string "Link list is empty."
        You should not include the value of dummy head or tail.

        Expected Output:
        firstElement  
        secondElement 
        ...
        """
        if self.size == 0:
            print("Link list is empty.")
        else:
            current = self.dummyHead.next
            while current != self.dummyTail:
                print(current.data)
                current = current.next


    def printFromBack(self):
        """
        Prints all elements of the linked list from back to front.
        If the linked list is empty, print exactly this string "Link list is empty."
        Follow the same format of printFromFront()
        """
        if self.size == 0:
            print("Link list is empty.")
        else:
            current = self.dummyTail.prev
            while current != self.dummyHead:
                print(current.data)
                current = current.prev


    def _isNodeUnbound(self,node):
        """
        A private method. 
        Check if the given node's linkage in the list is broken.
        This means the node does not appear in the traversal from head to tail.
        In the other words, check if the connection relation between the node 
        and the node before it is neutral. 
        Notice this method assumes all the methods related to delete a node are 
        implemented correctly. 

        Parameters
        ----------
        node : Node
            The node to check for broken linkage.

        Returns
        -------
        bool
            True if the node's linkage is broken, False otherwise.

        Example
        --------
        check if the next attribute of the node's previous node is 
        the node.
        """
        current = self.dummyHead
        while current.next != None:
            if current.next == node:
                return False
            current = current.next
        return True

    
    def getFront(self) -> int:
        """
        Returns the data from the first non dummy node in the linked list.

        Returns
        -------
        data or None
            The data of the first node in the list, or None if the list is empty.
            (size is zero)
        """
        return self.dummyHead.next.data if self.size > 0 else None

    def getBack(self) -> int:
        """
        Returns the data from the last non dummy node in the linked list.

        Returns
        -------
        data or None
            The data of the last node in the list, or None if the list is empty.
            (size is zero)
        """
        return self.dummyTail.prev.data if self.size > 0 else None
    
    def getSize(self) -> int:
        """
        Return the number of elements in the stack or queue.

        This method provides the current size of the linked list, 
        indicating how many elements are stored in it.

        Returns
        -------
        int
            The number of elements in linked list.
        """
        return self.size

if __name__ == "__main__":
    pass