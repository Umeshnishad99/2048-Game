import random
import constants as c

def new_game(n):
    matrix = []
    for i in range(n):
        matrix.append([0] * n)
    matrix = add_two(matrix)
    matrix = add_two(matrix)
    return matrix

def add_two(mat):
    a = random.randint(0, len(mat)-1)
    b = random.randint(0, len(mat)-1)
    while mat[a][b] != 0:
        a = random.randint(0, len(mat)-1)
        b = random.randint(0, len(mat)-1)
    mat[a][b] = 2
    return mat

def game_state(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 2048:
                return 'win'
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                return 'not over'
    for i in range(len(mat)-1):
        for j in range(len(mat[0])-1):
            if mat[i][j] == mat[i+1][j] or mat[i][j+1] == mat[i][j]:
                return 'not over'
    for k in range(len(mat)-1):
        if mat[len(mat)-1][k] == mat[len(mat)-1][k+1]:
            return 'not over'
    for j in range(len(mat)-1):
        if mat[j][len(mat)-1] == mat[j+1][len(mat)-1]:
            return 'not over'
    return 'lose'

# Move Functions

def reverse(mat):
    new = []
    for i in range(len(mat)):
        new.append([mat[i][len(mat[0])-j-1] for j in range(len(mat[0]))])
    return new

def transpose(mat):
    new = []
    for i in range(len(mat[0])):
        new.append([mat[j][i] for j in range(len(mat))])
    return new

def cover_up(mat):
    new = [[0] * len(mat[0]) for _ in range(len(mat))]
    done = False
    for i in range(len(mat)):
        count = 0
        for j in range(len(mat[0])):
            if mat[i][j] != 0:
                new[i][count] = mat[i][j]
                if j != count:
                    done = True
                count += 1
    return new, done

def merge(mat, done):
    for i in range(len(mat)):
        for j in range(len(mat[0])-1):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j+1] = 0
                done = True
    return mat, done

def up(mat):
    mat = transpose(mat)
    mat, done = cover_up(mat)
    mat, done = merge(mat, done)
    mat = cover_up(mat)[0]
    mat = transpose(mat)
    return mat, done

def down(mat):
    mat = reverse(transpose(mat))
    mat, done = cover_up(mat)
    mat, done = merge(mat, done)
    mat = cover_up(mat)[0]
    mat = transpose(reverse(mat))
    return mat, done

def left(mat):
    mat, done = cover_up(mat)
    mat, done = merge(mat, done)
    mat = cover_up(mat)[0]
    return mat, done

def right(mat):
    mat = reverse(mat)
    mat, done = cover_up(mat)
    mat, done = merge(mat, done)
    mat = cover_up(mat)[0]
    mat = reverse(mat)
    return mat, done

# Add a method to calculate score
def get_score(mat):
    return sum(sum(row) for row in mat)
