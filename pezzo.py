class Pezzo:
    def __init__(self, name, color, lPositions):
        self.name = name
        self.color = color
        self.pos=lPositions




    def __str__(self):
      return f'{self.name}:l={len(self.pos)}'

