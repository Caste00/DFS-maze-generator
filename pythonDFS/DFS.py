from random import shuffle
import time
import os
import sys

WALL = '██'
SPACE = '  '
PLAYER = '@@'

sys.setrecursionlimit(10000)

def creaGriglia(l, h) -> list:
    """
        Genera una griglia di dimensione l * h e ritorna un array
        bidimensionale della griglia
    """

    return [[WALL for _ in range(l)] for _ in range(h)]


def stampaGriglia(g):
    """
        Stampa il layout della griglia
    """
    x = len(g[0])
    y = len(g)

    for i in range(x + 2):
        if i == 1:
            print(SPACE, end="")
        else:
            print(WALL, end="")
    print()
        
    for i in range(y):
        print(WALL, end="")
        print("".join(g[i]), end="")
        print(WALL)
    
    for i in range(x + 2):
        if i == x:
            print(SPACE, end="")
        else:
            print(WALL, end="")
    print()
    
    
def generaLabirinto(l, h):
    g = creaGriglia(l, h)

    def rientra(x, y):
        return 0 <= x < h and 0 <= y <= l
            
    def genera(x, y) :
        stampaGriglia(g)
        time.sleep(0.01)
        os.system("clear")
        
        pos = [(0, 2), (0, -2), (2, 0), (-2, 0)]

        shuffle(pos)
                
        for nx, ny in pos:
            if rientra(nx + x, ny + y) and g[nx + x][ny + y] == WALL:
                g[x + nx][y + ny] = SPACE
                g[x + nx // 2][y + ny // 2] = SPACE
                genera(x + nx, y + ny)
        return

    genera(0, 0)
    return g
    

def player(g):
    x, y = 0, 0
    while True:
        pos = input("-> ")
        if pos == 'n':
            y -= 1
        elif pos == 's':
            y += 1
        elif pos == 'e':
            x += 1
        elif pos == 'o':
            x -= 1
        else:
            print("Mossa non valida, sono validi sono n, s, e, o")


def main():
    x = int(input("Inserire un numero dispari maggiore di 3: "))
    y = int(input("Inserire un numero dispari maggiore di 3: "))
    
    if x % 2 == 1 and x > 2 and y % 2 == 1 and y > 2:
        g = generaLabirinto(x, y)
        stampaGriglia(g)
    else:
        print("Errore, dimensioni inserite non valide")   


if __name__ == "__main__":
    main()
