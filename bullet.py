
from entity import Entity

class Bullet(Entity):
    """
    Represents a bullet in space invaders

    Methods :
        - trucs
    
    """
    def __init__(self ) -> None :
        self.damage = 1
        self.speed = 3