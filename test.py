class Board:

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
        if(self.board[row][col] != "-"):
            self.printBoard()
            newIndex = int(input("This position is taken. Input another: "))
            self.put(newIndex, value)
        else:
            self.board[row][col] = value

board = Board(3)

print("1 2 3")
print("4 5 6")
print("7 8 9")

while not board.isFull():
    value = int(input("Choose a position: "))
    board.put(value, "X")
    
