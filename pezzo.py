
class Pezzo:
    def __init__(self, name, color, lPositions):
        self.name = name
        self.color = color
        self.pos = lPositions

    def __str__(self):
        return f'{self.name}:l={len(self.pos)}'

    # data una tupla di cordinate
    # relative (x,y) genera una tupla ruotata di 90 gradi a destra

    def rotpos(self, xy):
        x, y = xy
        a = 0
        if x > 0 and y == 0:
            return (y, -x)
            a = a+1
        if x == 0 and y < 0:
            return (y, x)
            a = a+1

        if x < 0 and y == 0:
            return (y, -x)
            a = a+1

        if x == 0 and y > 0:
            return (y, x)
            a = a+1

    def rotate(self):
        lRotpos = list(map(self.rotpos, self.pos))
        self.pos = lRotpos
        return (self)

    # with this function I'm positionating my piece on the table based on the table start point

    def positionate(self, xy, rc):
        x, y = xy
        r, c = rc
        x = x+r
        y = y+c
        return (x, y)

    def visible_row(self, rc):
        """Controlla se la riga è visibile (r>=0)"""
        r, _ = rc
        return (r >= 0)

    def positionate_piece(self, rc):
        """
        Calcola i valori riga e colonna di tutti i pixel
        di un pezzo, passando una tupla (rc) che è la positione
        del pezzo zero.

        I valori negativi di riga, se presenti, vengono eliminati. 
        """
        abs_pos = map(
            lambda xy: self.positionate(xy, rc),
            self.pos)
        abs_pos_non_negative = filter(
            self.visible_row,
            abs_pos

        )
        return (list(abs_pos_non_negative))


# riga gialla
RIGA = Pezzo("-", "r", [(-1, 0), (0, 0), (1, 0), (2, 0)])
# S: verde
ESSE = Pezzo("s", "g", [(0, 0), (0, 1), (1, -1), (1, 0)])
# Z: rossa
ZETA = Pezzo("z", "b", [(0, -1), (0, 0), (1, 0), (1, 1)])
# L: arancione
ELLE = Pezzo("l", "o", [(0, -1), (0, 0), (1, 0), (1, 1)])
# Gamma (L rovesciata): blu
GAMM = Pezzo("rl", "b", [(0, -1), (0, 0), (1, 0), (1, 1)])
# T: violetta
TI = Pezzo("t", "p", [(0, -1), (0, 0), (1, 0), (1, 1)])
# Quadrato giallo
QUAD = Pezzo("q", "g", [(0, -1), (0, 0), (1, 0), (1, 1)])
