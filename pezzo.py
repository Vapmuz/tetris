"""file che rachiude tutte le funzioni collegate ai pezzi"""


class Pezzo:
    """Classe creata per racchiudere tutte le funzioni dei pezzi"""

    def __init__(self, name, color, l_position):
        self.name = name
        self.color = color
        self.pos = l_position

    def __str__(self):
        return f"{self.name}:l={len(self.pos)}"

    # data una tupla di cordinate
    # relative (x,y) genera una tupla ruotata di 90 gradi a destra

    def rotpos(self, xy):
        """questa funzione dato un punto nello spazio lo ruota"""
        x, y = xy
        if x > 0 and y == 0:
            return (y, -x)
        if x == 0 and y < 0:
            return (y, x)
        if x < 0 and y == 0:
            return (y, -x)
        if x == 0 and y > 0:
            return (y, x)

    def rotate(self):
        """questa funzione ruota un pezzo"""
        l_rotpos = list(map(self.rotpos, self.pos))
        self.pos = l_rotpos
        return self

    def positionate(self, xy, rc):
        """
        con questa funzione data la posizione relativa del pezzo trovo la  sua posizione assoluta
        """
        x, y = xy
        r, c = rc
        x = x + r
        y = y + c
        return (x, y)

    def visible_row(self, rc):
        """Controlla se la riga è visibile (r>=0)"""
        r, _ = rc
        return r >= 0

    def positionate_piece(self, rc):
        """
        Calcola i valori riga e colonna di tutti i pixel
        di un pezzo, passando una tupla (rc) che è la posizione
        del pezzo zero.

        I valori negativi di riga, se presenti, vengono eliminati.
        """
        abs_pos = map(lambda xy: self.positionate(xy, rc), self.pos)
        abs_pos_non_negative = filter(self.visible_row, abs_pos)
        return list(abs_pos_non_negative)


# riga gialla
I = Pezzo("-", "r", [(0, 1), (0, 0), (0, -1), (0, -2)])
# S: verde
Z = Pezzo("s", "g", [(0, -1), (0, 0), (1, 0), (1, 1)])
# Z: rossa (cambiare)
S = Pezzo("z", "b", [(0, -1), (0, 0), (-1, 0), (-1, 1)])
# L: arancione
L = Pezzo("l", "o", [(1, 0), (0, 0), (2, 0), (2, 1),])
# Gamma (L rovesciata): blu
J = Pezzo("rl", "b", [(1, 0), (0, 0), (2, 0), (2, -1)])
# T: violetta
T = Pezzo("t", "p", [(0, 1), (0, 0), (0, -1), (1, 0)])
# Quadrato giallo
O = Pezzo("q", "g", [(0, 1), (0, 0), (-1, 0), (-1, 1)])
# pezzo speciale test colonne
RIGA_TEST = Pezzo("-", "r", [(0, -1), (0, 0), (0, 1), (0, 2)])
