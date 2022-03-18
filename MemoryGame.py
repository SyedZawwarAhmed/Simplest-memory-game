import random
board_upper = [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"]]
words = ['A', 'A','B','B','C','C','D','D','E','E','F','F','G','G','H','H']
random.shuffle(words)
board = []
count = 0
row = []
for item in words:
    row.append(item)
    count += 1
    if count % 4 == 0:
        board.append(row)
        row = []

# make a function to print the board
def print_board(board):
    for row in board:
        for character in row:
            print(character, end=" ")
        print()

unmatched_pairs = 8

while unmatched_pairs > 0:
    print_board(board_upper)
    print("\n")
    print("Enter the coordinates for your first letter.")
    x1 = int(input("X (1-4): ")) - 1
    y1 = int(input("Y (1-4): ")) - 1
    print("First letter is: " + board[y1][x1])
    print("Enter the coordinates for your second letter.")
    while True:
        x2 = int(input("X (1-4):")) - 1
        y2 = int(input("Y (1-4):")) - 1
        if x2 != x1 or y2 != y1:
            break
        else:
            print("Second letter should not be the first letter.")
    print("Second letter is: " + board[y2][x2])
    if board[y1][x1] == board[y2][x2]:
        print("matched")
        board_upper[y1][x1] = board[y1][x1]
        board_upper[y2][x2] = board[y2][x2]
        unmatched_pairs -= 1
    else:
        print("\n")
        print("Try again.")
        print("\n")

print("Congratulations! You found all the pairs!")