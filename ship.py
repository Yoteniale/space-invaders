from typing import Self
from entity import Entity
from bullet import Bullet

class Ship(Entity, Bullet):
    """
    Reprensents a ship in space invaders

    Methods :
        - trucs
        -
    """
    def __init__(self : Self) -> None:
        self.__hp = 10
        self.damage = Bullet.damage
        self.speed = 10

    def on_hit(self : Self , damage : int) -> None :
        self.__hp -= damage
        print(self.pseudo, "suffered", damage, "points of damage.")

    def hit(self : Self, other : Self) -> None :
        other.on_hit(self.damage)



class Player(Ship):
    """
    Represents a player in space invaders
    
    Methods : 
        - trucs
        -
    """
    def __init__(self : Self, pseudo : int) -> None:
        self.pseudo = pseudo
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
    def __init__(self : Self) -> None:
        self.pseudo = "alien"
        self.hp = 10
        self.speed = 5    

    def die(self : Self) -> None :
        ...

    def on_hit(self, damage) -> None:
        if self.hp < damage :
            return self.die()
        return super().on_hit(damage)