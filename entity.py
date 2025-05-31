from math import sqrt

class Entity :
    """
    Represents an entity in space invaders

    Methods: 
        - .move() : 
    
    """
    def __init__(self ):
        ...

    def move(self, hor : int , ver : int, vel : int):
        """
        updates position based on horizontal (hor) and/or vertical (ver) directions and velocity (vel) parameter
        """

        x, y  = 0, 0
        if hor != 0 and ver != 0 :
            vel /= sqrt(2)
            print(vel)
        if hor > 0 :
            x += vel
        if ver > 0 :
            y += vel
        if hor < 0:
            x -= vel
        if ver < 0:
            y -= vel

        return x,y

if __name__ == '__main__':
    E = Entity()
    u , v = 2, 3
    a, b = E.move(-1, -1, 7)
    u += a
    v += b
    print(u, v )