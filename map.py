from enemy import Enemy
import random
import pickle

class Map:
    def __init__(self, height=10, width=10, enemies=4):
        self.height = height
        self.width = width
        self.enemies = enemies

        map = [0 for i in range(height) for i in range(width)]
        while enemies != 0:
            for row in map:
                for col in map:
                    if random.randint(0, 100) < 50:
                        map[row][col] = MapCell(col, row, Enemy(col*row, f"Enemy at [{col}, {row}]", 10, 5))
                    else:
                        map[row][col] = MapCell(col, row)

    def pickle(self) -> bytes:
        return pickle.dumps(self)

class MapCell:
    def __init__(self, x: int, y: int, enemy: Enemy = None):
        self.x = x
        self.y = y

        if self.enemy:
            self.enemy = enemy
        else:
            self.enemy = None