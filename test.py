class Board:

    wins = None
    board = None
    taken = None
    size = 0

    def __init__(self, size):
        self.board = []
        for i in range(size):
            temp = ["-"] * size
            self.board.append(temp)
        self.taken = [None] * (size * size)
        self.size = size
        self.wins = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

    def printBoard(self):
        for i in range(self.size):
            for t in range(self.size):
                print(self.board[i][t]," ")

    def isFull(self):
        for i in range(0, self.size):
            for t in range(0, self.size):
                if self.board[i][t] == "-":
                    return False
        return True
    def size(self):
        return self.size

    def put(self,index, value):
        row = None
        if(index % self.size == 0):
            row = index//self.size - 1
        else:
            row = index//self.size
        col = index % self.size - 1
        self.board[row][col] = value
    def playerMove(self):
        value = int(input("Choose a square (1-9): "))
        while self.taken[value]:
            value = int(input("Invalid square (1-9): "))
        self.put(value, "X")
        self.taken[value] = "X"

    def aiMove(self):
        temp = 0
        while not self.taken[temp]:
            temp += 1
        self.put(temp, "O")
        self.taken[temp] = "O"

    def hasWin(self,letter):
        hasWin = False
        array = []
        for value in self.taken:
            if(value == letter):
                array.append(self.taken.index(value))
        
        for trio in self.wins:
            if set(trio).issubset(set(array)):
                hasWin = True
        return hasWin


board = Board(3)

print("1 2 3")
print("4 5 6")
print("7 8 9")

while not board.isFull():
    board.printBoard()
    board.playerMove()
    if(board.hasWin("X")):
        print("You won!")
        break
    board.printBoard()
    board.aiMove()
    if(board.hasWin("O")):
        print("AI won!")
        break
    

