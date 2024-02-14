from enum import Enum

'''
This is the start of the HW.
If there is any conflict between the doc string and the HW document,
please follow the instruction in the HW document.
Good Luck and have fun !
'''

class Notation(Enum):
    """Enumeration for representing different types of notations in the game.

    Attributes:
        EMPTY (int): Represents an empty cell on the board.
        PLAYER1 (int): Represents a cell occupied by Player 1.
        PLAYER2 (int): Represents a cell occupied by Player 2.
    """
    EMPTY = 0
    PLAYER1 = 1
    PLAYER2 = 2

class Player:
    """Represents a player in the game.

    Attributes:
        __playerName (str): The name of the player.
        __playerNotation (Notation): The notation (symbol) used by the player on the board.
        __curScore (int): The current score of the player.

    Args:
        playerName (str): The name of the player.
        playerNotation (Notation): The notation (symbol) used by the player.
        curScore (int): The initial score of the player.
    """
    __playerName: str
    __playerNotation: Notation
    __curScore: int

    def __init__(self, playerName, playerNotation, curScore):
        self.__playerName = playerName
        self.__playerNotation = playerNotation
        self.__curScore = curScore

    def display(self) -> str:
        """Displays the player's details including name, notation, and current score."""
        return f'Player Name: {self.__playerName}, Notation: {self.__playerNotation}, Score: {self.__curScore}'

    def addScoreByOne(self):
        """Increments the player's score by one."""
        self.__curScore += 1

    def getScore(self):
        """Returns the current score of the player."""
        return self.__curScore

    def getName(self):
        """Returns the name of the player."""
        return self.__playerName

    def getNotation(self):
        """Returns the notation used by the player."""
        return self.__playerNotation

class Board:
    """Represents the game board.

    Attributes:
        __rowNum (int): Number of rows in the board.
        __colNum (int): Number of columns in the board.
        __grid (list): 2D list representing the game board.

    Args:
        rowNum (int): Number of rows in the board.
        colNum (int): Number of columns in the board.
    """
    __rowNum: int
    __colNum: int
    __grid: list

    def __init__(self, rowNum, colNum) -> None:
        self.__rowNum = rowNum
        self.__colNum = colNum
        self.initGrid()

    def initGrid(self):
        """Initializes the game board with empty cells."""
        self.__grid = [[Notation.EMPTY] * self.__colNum for _ in range(self.__rowNum)]

    def getColNum(self):
        """Returns the number of columns in the board."""
        return self.__colNum

    def placeMark(self, colNum, mark):
        """Attempts to place a mark on the board at the specified column.

        Args:
            colNum (int): The column number where the mark is to be placed.
            mark (Notation): The mark to be placed on the board.

        Returns:
            bool: True if the mark was successfully placed, False otherwise.
        """
        if colNum < 0 or colNum >= self.__colNum:
            print('Invalid column number')
            return False
        if mark != Notation.PLAYER1 and mark != Notation.PLAYER2:
            print('Invalid marker')
            return False
        for i in range(self.__rowNum - 1, -1, -1):
            if self.__grid[i][colNum] == Notation.EMPTY:
                self.__grid[i][colNum] = mark
                return True
        print('Column is full')
        return False

    def checkFull(self):
        """Checks if the board is completely filled.

        Returns:
            bool: True if the board is full, False otherwise.
        """
        for row in self.__grid:
            for cell in row:
                if cell == Notation.EMPTY:
                    return False
        return True

    def display(self):
        """Displays the current state of the board."""
        boardStr = ''
        for row in self.__grid:
            for cell in row:
                if cell == Notation.EMPTY:
                    boardStr += 'O'
                elif cell == Notation.PLAYER1:
                    boardStr += 'R'
                else:
                    boardStr += 'Y'
            boardStr += '\n'
        print('Current Board is\n' + boardStr)

    # Private methods for internal use
    def __checkWinHorizontal(self, target):
        """Checks if there is a winning condition in the horizontal direction.
        
        Args:
            target (int): The number of consecutive marks needed for a win.
        
        Returns:
            Notation or None: The notation of the winning player, or None if there is no winner.
        """
        for row in range(self.__rowNum):
            for col in range(self.__colNum):
                if self.__grid[row][col] == Notation.EMPTY:
                    continue
                if col <= self.__colNum - target:
                    if all([self.__grid[row][col + i] == self.__grid[row][col] for i in range(target)]):
                        return self.__grid[row][col]
        return None

    def __checkWinVertical(self, target):
        """Checks if there is a winning condition in the vertical direction.
        
        Args:
            target (int): The number of consecutive marks needed for a win.
        
        Returns:
            Notation or None: The notation of the winning player, or None if there is no winner.
        """
        for col in range(self.__colNum):
            for row in range(self.__rowNum):
                if self.__grid[row][col] == Notation.EMPTY:
                    continue
                if row <= self.__rowNum - target:
                    if all([self.__grid[row+i][col] == self.__grid[row][col] for i in range(target)]):
                        return self.__grid[row][col]
        return None

    def __checkWinOneDiag(self, target, rowNum, colNum):
        """Checks if there is a winning condition in the diagonal direction from the current cell.
        
        Args:
            target (int): The number of consecutive marks needed for a win.
            rowNum (int): The row number of the current cell.
            colNum (int): The column number of the current cell.
            
        Returns:
            Notation or None: The notation of the winning player, or None if there is no winner."""
        if rowNum < target - 1 or colNum >= self.__colNum - target + 1:
            return None
        player = self.__grid[rowNum][colNum]
        for i in range(target):
            if self.__grid[rowNum - i][colNum + i] != player:
                return None
        return player


    def __checkWinAntiOneDiag(self, target, rowNum, colNum):
        """Checks if there is a winning condition in the nti-diagonal direction from the current cell.
        
        Args:
            target (int): The number of consecutive marks needed for a win.
            rowNum (int): The row number of the current cell.
            colNum (int): The column number of the current cell.
            
        Returns:
            Notation or None: The notation of the winning player, or None if there is no winner.
        """
        if rowNum < target - 1 or colNum < target - 1:
            return None
        player = self.__grid[rowNum][colNum]
        for i in range(target):
            if self.__grid[rowNum - i][colNum - i] != player:
                return None
        return player

    def __checkWinDiagonal(self, target):
        """Checks if there is a winning condition in the diagonal direction.
        
        Args:
            target (int): The number of consecutive marks needed for a win.

        Returns:
            Notation or None: The notation of the winning player, or None if there is no winner.
        """
        for row in range(self.__rowNum):
            for col in range(self.__colNum):
                if self.__grid[row][col] == Notation.EMPTY:
                    continue
                winnerDiag = self.__checkWinOneDiag(target, row, col)
                winnerXDiag = self.__checkWinAntiOneDiag(target, row, col)
                if winnerDiag or winnerXDiag:
                    return winnerDiag or winnerXDiag
        return None
    
    def checkWin(self, target):
        """Checks if there is a winning condition on the board.

        Args:
            target (int): The number of consecutive marks needed for a win.

        Returns:
            Notation or None: The notation of the winning player, or None if there is no winner.
        """
        return self.__checkWinHorizontal(target) or self.__checkWinVertical(target) or self.__checkWinDiagonal(target)

class Game:
    """Represents the game logic and flow.

    Args:
        rowNum (int): Number of rows in the game board.
        colNum (int): Number of columns in the game board.
        connectN (int): Number of consecutive marks needed for a win.
        targetScore (int): The score a player needs to reach to win the game.
        playerName1 (str): Name of the first player.
        playerName2 (str): Name of the second player.
    """
    __board: Board
    __connectN: int
    __targetScore: int
    __playerList: list
    __curPlayer: Player

    def __init__(self, rowNum, colNum, connectN, targetScore, playerName1, playerName2) -> None:
        self.__board = Board(rowNum, colNum)
        self.__connectN = connectN
        self.__targetScore = targetScore
        self.__playerList = [Player(playerName1, Notation.PLAYER1, 0), Player(playerName2, Notation.PLAYER2, 0)]
        self.__curPlayer = self.__playerList[0]

    def __playBoard(self, curPlayer):
        """Handles the process of a player making a move on the board.

        Args:
            curPlayer (Player): The current player who is making the move.
        """
        isPlaced = False
        while not isPlaced:
            try:
                colNum = int(input(f'{curPlayer.getName()}, please input a column number: '))
            except ValueError:
                print('Invalid column number')
                continue
            if colNum < 0 or colNum >= self.__board.getColNum():
                print('Invalid column number')
                continue
            if self.__board.placeMark(colNum, curPlayer.getNotation()):
                isPlaced = True

    def __changeTurn(self):
        """Switches the turn to the other player."""
        self.__curPlayer = self.__playerList[0] if self.__curPlayer == self.__playerList[1] else self.__playerList[1]

    def playRound(self):
        """Plays a single round of the game."""
        curWinnerNotation = None
        self.__board.initGrid()
        self.__curPlayer = self.__playerList[0]
        print('Starting a new round')
        while not curWinnerNotation:
            self.__board.display()
            self.__playBoard(self.__curPlayer)
            curWinnerNotation = self.__board.checkWin(self.__connectN)
            if curWinnerNotation:
                print(f'{self.__curPlayer.getName()} wins!')
                self.__board.display()
                self.__curPlayer.addScoreByOne()
                break
            if self.__board.checkFull():
                print('Board is full, no winner for this round')
                break
            self.__changeTurn()

    def play(self):
        """Starts and manages the game play until a player wins."""
        while self.__playerList[0].getScore() < self.__targetScore and self.__playerList[1].getScore() < self.__targetScore:
            self.playRound()
        print('Game Over')
        print(self.__playerList[0].display())
        print(self.__playerList[1].display())

def main():
    """Main function to start the game."""
    game = Game(4, 4, 3, 2, 'P1', 'P2')
    game.play()

if __name__ == "__main__":
    main()