import numpy as np
import random
import hashlib
from jelly.configs import GRID_LENGTH

def get_status(bombs, row0, col0, row1, col1):
    n = GRID_LENGTH
    grid_status = np.ones((n,n))
    delete_position = list()
    delete_pair = set()
    for i in range(row0,row1+1):
        for j in range(col0,col1+1):
            delete_position.append((i,j))
            delete_pair.add((i,j))
    for pair in delete_position:
        i, j = pair
        grid_status[i,j] = 0
        if bombs[get_str_num(i,j)] == 'H':
            for c in range(n):
                if (i,c) not in delete_pair:
                    grid_status[i,c] = 0
                    delete_position.append((i,c))
                    delete_pair.add((i,c))
        elif bombs[get_str_num(i,j)] == 'V':
            for r in range(n):
                if (r,j) not in delete_pair:
                    grid_status[r,j] = 0
                    delete_position.append((r,j))
                    delete_pair.add((r,j))
        elif bombs[get_str_num(i,j)] == 'S':
            for r in range(i - 1, i + 2):
                for c in range(j - 1, j + 2):
                    if r<0 or r>n-1 or c<0 or c>n-1:
                        continue
                    if (r,c) not in delete_pair:
                        grid_status[r,c] = 0
                        delete_position.append((r,c))
                        delete_pair.add((r,c))
    #print(grid_status)
    bombs_list = list(bombs)
    for j in range(n):
        void = 0
        for i in range(n-1,-1,-1):
            position = get_str_num(i,j)
            if grid_status[i][j] == 1:
                if void > 0:
                    new_position = get_str_num(i + void, j)
                    bombs_list[new_position] = bombs_list[position]
                    bombs_list[position] = 'N'
            else:
                void += 1
                #print(j,void)
                bombs_list[position] = 'N'
    for i,b in enumerate(bombs_list):
        if b == 'N':
            bombs_list[i] = random.choice('BSVH')
    bombs = ''.join(bombs_list)
    return bombs

def get_str_num(row, col):
    n = GRID_LENGTH 
    number = row * n + col
    return number

def get_grid_str():
    n = GRID_LENGTH
    bombs_list = list()
    for i in range(n * n):
        bombs_list.append(random.choice('BSVH'))
    return ''.join(bombs_list)

def get_hash_str(bombs):
    hash = hashlib.md5()
    hash_str = hashlib.md5(bytes(bombs,encoding='utf-8'))
    return hash_str.hexdigest()
    

#b = get_status('VSBBSBBBHBBBBBBBBSBBBBBBBBBBVBBBBHBBBBBBSBBBBSBBBBBBBBBBBBBBBBBB',5,0,6,2)
#print(b)
