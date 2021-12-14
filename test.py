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
            print(self.board[i]," ")

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
            col = self.size - 1
        else:
            row = index//self.size
            col = index % self.size - 1
        self.board[row][col] = value
        self.taken[index - 1] = value

    def playerMove(self):
        value = int(input("Choose a square (1-9): "))
        while self.taken[value - 1]:
            value = int(input("Invalid square (1-9): "))
        self.put(value, "X")

    def aiMove(self):
        temp = 0
        while temp < len(self.taken) and self.taken[temp]:
            temp += 1
        self.put(temp + 1, "O")

    def state(self,letter):
        array = self.positions(letter)
        for trio in self.wins:
            if trio[0] in array and trio[1] in array and trio[2] in array:
                return 10
        opponent = None
        if letter == "X":
            opponent = "O"
        else:
            opponent = "O"
        array = self.positions(opponent)
        for trio in self.wins:
            if trio[0] in array and trio[1] in array and trio[2] in array:
                return -10
        tie = True
        for i in range(len(self.taken)):
            if self.taken[i] == None:
                tie = False
        if tie:
            return 0
        return 1

    def positions(self, letter):
        array = []
        for i in range(len(self.taken)):
            if(self.taken[i] == letter):
                array.append(i + 1)
        return array

    def minimax(self, depth, player):
        if self.state(player) != 0:
            return self.state(player)
        moves = self.positions("-")
        if player == "X":
            opponent = "O"
            bestVal = -20
            for move in moves:
                self.board.put(move, "X")
                val = self.minimax(depth + 1, opponent)
                self.board.put(move, "-")
                if val > bestVal:
                    bestVal = val
            return bestVal
        else:
            opponent = "X"
            bestVal = 20
            for move in moves:
                self.board.put(move, "O")
                val = self.minimax(depth + 1, opponent)
                self.board.put(move, "-")
                if val < bestVal:
                    bestVal = val
            return bestVal



board = Board(3)

print("1 2 3")
print("4 5 6")
print("7 8 9")

while True:
    board.printBoard()
    board.playerMove()
    if(board.state("X") == 0):
        print("Tie!")
        break
    elif(board.state("X") == 10):
        print("You won!")
        break
    board.aiMove()
    if(board.state("O") == 10):
        print("AI won!")
        break
    elif(board.state("O") == 0):
        print("Tie!")
        break
