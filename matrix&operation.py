from collections import deque

def solution(rc, operations):
    for op in operations:
        if op == 'Rotate':
            rc = rotate(rc)
        elif op == 'ShiftRow':
            rc = shiftRow(rc)
        else:
            continue
    return rc

def rotate(rc):
    return setAround(rc, getAround(rc))

def getAround(rc):
    row = len(rc)
    col = len(rc[0])
    queue = deque()
    for i in range(col-1):
        queue.append(rc[0][i])
    for i in range(row-1):
        queue.append(rc[i][col-1])
    for i in range(col-1, 0, -1):
        queue.append(rc[row-1][i])
    for i in range(row-1, 0, -1):
        queue.append(rc[i][0])
    return queue

def setAround(rc, queue):
    row = len(rc)
    col = len(rc[0])
    for i in range(1, col):
        rc[0][i] = queue.popleft()
    for i in range(1, row):
        rc[i][col-1] = queue.popleft()
    for i in range(col-2, -1, -1):
        rc[row-1][i] = queue.popleft()
    for i in range(row-2, -1, -1):
        rc[i][0] = queue.popleft()
    return rc

DeprecationWarning
def rotate(rc):
    first = rc[0][0]
    for i in range(len(rc)-1):
        rc[i][0] = rc[i+1][0]
    for i in range(len(rc[len(rc)-1])-1):
        rc[len(rc)-1][i] = rc[len(rc)-1][i+1]
    for i in range(len(rc)-1, 0, -1):
        rc[i][len(rc[len(rc)-1])-1] = rc[i-1][len(rc[len(rc)-1])-1]
    for i in range(len(rc[0])-1, 0, -1):
        rc[0][i] = rc[0][i-1]
    rc[0][1] = first
    return rc

def shiftRow(rc):
    return [rc[-1]] + rc[0:-1]

rc = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
operations = ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]

print(solution(rc, operations))