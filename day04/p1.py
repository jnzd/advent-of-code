
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
    
    won = False
    winningBoard = None
    while not won:
        for board in boards:
            if checkBoard(board, winningNumbers):
                won = True
                winningBoard = sum(board, [])
                winningNumber = winningNumbers[-1]
                break
        if not won:
            winningNumbers = winningNumbers + numbers[:1]
            numbers = numbers[1:]
    
    res = list(filter(lambda x: x not in winningNumbers, winningBoard))
    res = sum(res, 0) * winningNumber
    print(res)
