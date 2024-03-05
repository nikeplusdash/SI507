class TwentyQuestions:
    def __init__(self):
        """
        Initialize the TwentyQuestions class with predefined small and medium trees.
        Sets the current tree to the small tree by default.
        """
        self.smallTree = (
            "Is it bigger than a breadbox?",
            ("an elephant", None, None),
            ("a mouse", None, None),
        )
        self.mediumTree = (
            "Is it bigger than a breadbox?",
            ("Is it gray?", ("an elephant", None, None), ("a tiger", None, None)),
            ("a mouse", None, None),
        )
        self.currentTree = self.smallTree  # Default tree

    def inputChecker(self, userIn: str):
        """
        aka(yes(userIn))
        Check if the user's input is an affirmative response.

        Parameters
        ----------
        userIn : str
            The input string from the user.

        Returns
        -------
        bool
            True if the input is an affirmative response ('y', 'yes', 'yup', 'sure'), else False.
        """
        if userIn.lower() in ["y", "yes", "yup", "sure"]:
            return True
        else:
            return False

    def checkIfLeaf(self, curNode):
        """
        Determine if the given node is a leaf node.

        Parameters
        ----------
        curNode : tuple
            The current node in the decision tree.

        Returns
        -------
        bool
            True if the node is a leaf (both children are None), else False.
        """
        if curNode[1] is None and curNode[2] is None:
            return True
        else:
            return False

    def simplePlay(self, curNode):
        """
        Conduct a simple playthrough of the game using the current node.

        Parameters
        ----------
        curNode : tuple
            The current node in the decision tree.

        Returns
        -------
        bool
            True if the player successfully guesses the item, else False.
        """
        if self.checkIfLeaf(curNode):
            print(f"Is it {curNode[0]}?")
            return self.inputChecker(input())
        print(curNode[0])
        if self.inputChecker(input()):
            return self.simplePlay(curNode[1])
        else:
            return self.simplePlay(curNode[2])

    def createNode(self, userQuestion: str, userAnswer: str, isCorrectForQues: bool, curNode: tuple):
        """
        Create a new node in the decision tree.

        Parameters
        ----------
        userQuestion : str
            The question to differentiate the new answer from the current node.
        userAnswer : str
            The answer provided by the user.
        isCorrectForQues : bool
            True if the userAnswer is the correct response to the userQuestion.
        curNode : tuple
            The current node in the decision tree at which the game has arrived. 
            This node typically represents the point in the game 
            where the player's guess was incorrect, 
            and a new question-answer pair needs to be 
            added to refine the tree. 


        Returns
        -------
        tuple
            The new node created with the user's question and answer 
            and curNode
        """
        if isCorrectForQues:
            return (userQuestion, (userAnswer, None, None), curNode)
        else:
            return (userQuestion, curNode, (userAnswer, None, None))

    def playLeaf(self, curNode):
        """
        Handle gameplay when a leaf node is reached in the decision tree. This method is called when 
        the game's traversal reaches a leaf node, indicating a guess at the player's thought. If the guess is 
        incorrect, the method prompts the player for the correct answer and a distinguishing question, creating a 
        new node in the tree to enhance future gameplay. It should call self.createNode(....)

        Parameters
        ----------
        curNode : tuple
            The current leaf node in the decision tree. A leaf node is represented as a tuple with the guessed 
            object as the first element and two `None` elements, signifying that it has no further branches.

        Returns
        -------
        tuple
            The updated node based on user input. If the player's response indicates that the initial guess was 
            incorrect, this method returns a new node that includes the correct answer and a new question 
            differentiating it from the guessed object. If the guess was correct, it simply returns the unchanged 
            `curNode`.
        
        Notes
        -----
        The method interacts with the player to refine the decision tree. It's a crucial part of the learning 
        aspect of the game, enabling the tree to expand with more nuanced questions and answers based on 
        player feedback.
        """
        print(f"Is it {curNode[0]}?")
        if self.inputChecker(input()):
            print("I got it!")
            return curNode
        else:
            print("Drats! What was it? ")
            userAnswer = input()
            print(f"What's a question that distinguishes between {curNode[0]} and {userAnswer}.")
            userQuestion = input()
            print(f"And what's the answer for {userAnswer}?")
            isCorrectForQues = self.inputChecker(input())
            return self.createNode(userQuestion, userAnswer, isCorrectForQues, curNode)


    def play(self, curNode):
        """
        Conduct gameplay starting from the given node.

        Parameters
        ----------
        curNode : tuple
            The current node in the decision tree.

        Returns
        -------
        tuple
            The updated tree after playing from the given node.
        """
        if self.checkIfLeaf(curNode):
            return self.playLeaf(curNode)
        print(curNode[0])
        if self.inputChecker(input()):
            return (curNode[0], self.play(curNode[1]), curNode[2])
        else:
            return (curNode[0], curNode[1], self.play(curNode[2]))

    def playRound(self):
        """
        Execute a single round of the game, starting from the current state of the currentTree attribute. This method 
        calls the 'play' method to navigate through the tree. It then updates the 'currentTree' 
        attribute with the potentially modified tree resulting from this round of gameplay.

  
        Returns
        -----
        None
        """
        self.currentTree = self.play(self.currentTree)


    def saveTree(self, node, treeFile):
        """
        Recursively save the decision tree to a file.

        Parameters
        ----------
        node : tuple
            The current node in the decision tree.
        treeFile : _io.TextIOWrapper
            The file object where the tree is to be saved.
        """
        if node is None:
            return
        if self.checkIfLeaf(node):
            print(f"Leaf\n{node[0]}", file=treeFile)
        else:
            print(f"Internal node\n{node[0]}", file=treeFile)
            self.saveTree(node[1], treeFile)
            self.saveTree(node[2], treeFile)


    def saveGame(self, treeFileName):
        """
        Save the current state of the game's decision tree to a specified file. This method opens the file 
        with the given filename and writes the structure of the current decision tree to it. The tree is saved 
        in a txt format.

        The method uses the 'saveTree' function to perform the recursive traversal and writing of the tree 
        structure. Each node of the tree is written to the file with its type ('Leaf' or 'Internal node') 
        followed by its content (question or object name). 
        
        Parameters
        ----------
        treeFileName : str
            The name of the file where the current state of the decision tree will be saved. The file will be 
            created or overwritten if it already exists.

        """
        with open(treeFileName, "w") as treeFile:
            self.saveTree(self.currentTree, treeFile)


    def loadTree(self, treeFile):
        """
        Recursively read a binary decision tree from a file and reconstruct it.

        Parameters
        ----------
        treeFile : _io.TextIOWrapper
            An open file object to read the tree from.

        Returns
        -------
        tuple
            The reconstructed binary tree.
        """
        line = treeFile.readline().strip()
        if line == "Leaf":
            return (treeFile.readline().strip(), None, None)
        else:
            question = treeFile.readline().strip()
            left = self.loadTree(treeFile)
            right = self.loadTree(treeFile)
            return (question, left, right)

    def loadGame(self, treeFileName):
        """
        Load the game state from a specified file and update the current decision tree. This method opens the 
        file with the given filename and reconstructs the decision tree based on its contents. 

        The method employs the 'loadTree' function to perform recursive reading of the tree structure from the 
        file. Each node's type ('Leaf' or 'Internal node') and content (question or object name) are read and 
        used to reconstruct the tree in memory. This restored tree becomes the new 'self.currentTree' of the game.

        Parameters
        ----------
        treeFileName : str
            The name of the file from which the game state will be loaded. The file should exist and contain a 
            previously saved decision tree.

        """
        with open(treeFileName, "r") as treeFile:
            self.currentTree = self.loadTree(treeFile)


    def printTree(self):
        self._printTree(tree = self.currentTree)

    def _printTree(self, tree, prefix = '', bend = '', answer = ''):
        """Recursively print a 20 Questions tree in a human-friendly form.
        TREE is the tree (or subtree) to be printed.
        PREFIX holds characters to be prepended to each printed line.
        BEND is a character string used to print the "corner" of a tree branch.
        ANSWER is a string giving "Yes" or "No" for the current branch."""
        text, left, right = tree
        if left is None  and  right is None:
            print(f'{prefix}{bend}{answer}It is {text}')
        else:
            print(f'{prefix}{bend}{answer}{text}')
            if bend == '+-':
                prefix = prefix + '| '
            elif bend == '`-':
                prefix = prefix + '  '
            self._printTree(left, prefix, '+-', "Yes: ")
            self._printTree(right, prefix, '`-', "No:  ")

def main():
    '''
    The main function to play the game. It initializes the game,
    loads a tree from a file if the user wants, plays the game,
    and saves the tree to a file if the user wants.
    '''
    print("Welcome to 20 Questions!")
    game = TwentyQuestions()

    # Load a tree from a file if the user wants else use the small tree
    load_from_file = input("Would you like to load a tree from a file? ")
    if load_from_file.lower() in ["y", "yes", "yup", "sure"]:
        tree_file = input("What's the name of the file? ")
        game.loadGame(tree_file)
        # game.printTree()
    else:
        game.currentTree = game.smallTree

    # Play the game
    play_again = True
    while play_again:
        game.playRound()
        play_again_input = input("Would you like to play again? ")
        play_again = play_again_input.lower() in ["y", "yes", "yup", "sure"]

    # Save the tree to a file if the user wants
    save_to_file = input("Would you like to save this tree for later? ")
    if save_to_file.lower() in ["y", "yes", "yup", "sure"]:
        tree_file = input("Please enter a file name: ")
        game.saveGame(tree_file)
        print(f"Thank you! The file has been saved.")

    # End the game
    print("Bye!")

if __name__ == '__main__':
    main()
