n = int(input("Enter number of rows: "))
board = [["." for __ in range(n)] for _ in range(n)]
result = []

marked_row = [False for _ in range(n)]
marked_col = [False for _ in range(n)]
right_diagonal = set()
left_diagonal = set()


def safe(r, c):
    for i in range(r):
        if board[i][c] == 'M':
            return False

    i, j=r-1, c-1
    while i>=0 and j>=0:
        if board[i][j]=='M':
            return False
        i-=1
        j-=1


    i,j=r-1, c+1
    while i>=0 and j<n:
        if board[i][j]=='M':
            return False
        i-=1
        j+=1

    return True


def solve(r):
    if r >= n:
        result.append(["".join(row) for row in board])
        return
    for j in range(n):
        if safe(r, j):
            board[r][j] = "M"
            solve(r + 1)
            board[r][j] = "."


solve(0)
if len(result)>0:
    print(result[0])
else:
    print(result)
