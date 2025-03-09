from typing import Self
from entity import Entity

class Bullet(Entity):
    """
    Represents a bullet in space invaders

    Methods :
        - trucs
    
    """
    def __init__(self : Self) -> None :
        self.damage = 1
        self.speed = 3