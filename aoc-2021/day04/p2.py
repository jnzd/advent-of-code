
def columns(board):
    return list(map(list, list(zip(*board[::-1]))))

def checkRow(row, numbers):
    return all(n in numbers for n in row)

def checkRows(board, numbers):
    return any(checkRow(row, numbers) for row in board)

def checkColumn(column, numbers):
    return all(n in numbers for n in column)

def checkColumns(board, numbers):
    return any(checkColumn(column, numbers) for column in columns(board))

def checkBoard(board, numbers):
    return checkRows(board, numbers) or checkColumns(board, numbers)


with open("in.txt", "r") as f:
    numbers, *boards = list(filter(lambda x: len(x) > 0, f.read().splitlines()))
    numbers = numbers.split(",")
    numbers = list(map(int, numbers))
    # print(numbers)
    boards = [boards[i:i+5] for i in range(0, len(boards), 5)]
    boards = list(map(lambda board: list(map(lambda row: row.split(), board)), boards))
    boards = list(map(lambda board: list(map(lambda row: list(map(int, row)), board)), boards))
    # print(boards)
    

    winningNumbers = numbers[:1]
    numbers = numbers [1:] 


    lastWinningNumbers = None
    lastWinningNumber = None
    lastWinningBoard = None
    while len(numbers) > 0:
        for board in boards:
            if checkBoard(board, winningNumbers):
                print(*boards, sep="\n")
                print("\n")
                lastWinningBoard = sum(board, [])
                lastWinningNumber = winningNumbers[-1]
                lastWinningNumbers = winningNumbers
                boards.remove(board)
        winningNumbers = winningNumbers + numbers[:1]
        numbers = numbers[1:]
    
    res = list(filter(lambda x: x not in lastWinningNumbers, lastWinningBoard))
    res = sum(res, 0) * lastWinningNumber
    print(lastWinningNumbers)
    print(lastWinningBoard)
    print(res)
