import pygame
import math
from npc import Npc
import random
import globals
#test

class Ghost(Npc):
    def __init__(self, x, y):
        super().__init__(x, y, "assets/characters/ghost")
        self.health = 1
        self.moveSpeed = 1

