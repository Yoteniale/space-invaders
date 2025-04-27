#from typing import Self
from entity import Entity
from bullet import Bullet

class Ship(Entity):
    """
    Reprensents a ship in space invaders

    Methods :
        - trucs
        -
    """
    def __init__(self ) -> None:
        self.__hp = 10
        self.damage = Bullet.damage
        self.speed = 10

    def on_hit(self  , damage : int) -> None :
        self.__hp -= damage
        print(self.pseudo, "suffered", damage, "points of damage.")

    def hit(self , other ) -> None :
        other.on_hit(self.damage)






class Player(Ship):
    """
    Represents a player in space invaders
    
    Methods : 
        - trucs
        -
    """
    def __init__(self ) -> None:
        self.pseudo = "Player"
        self.hp = 8
        self.speed = 10

    def on_hit(self, damage) -> None :
        if self.hp < damage :
            return print("You have died :(")
        return super().on_hit(damage)





class Nemesis(Ship):
    """
    Represents an ennemi in space invaders
    
    Methods : 
        - trucs
        -
    """
    def __init__(self ) -> None:
        self.pseudo = "alien"
        self.hp = 10
        self.speed = 5    

    def die(self ) -> None :
        ...

    def on_hit(self, damage) -> None:
        if self.hp < damage :
            return self.die()
        return super().on_hit(damage)
    




if __name__ == '__main__':
    P = Player("p")
    u , v = 2, 3
    u, v = P.move(-1, -1, 7)
    print(u, v )