from typing import Self 

class Entity :
    """
    Represents an entity in space invaders

    Methods: 
        - trucs
    
    """

if __name__ == '__main__':
    E = Entity()
    u , v = 2, 3
    a, b = E.move(-1, -1, 7)
    u += a
    v += b
    print(u, v )