"""file che racchiude tutte le funzioni collegate ai pezzi"""


class Pezzo:
    """Classe creata per racchiudere tutte le funzioni dei pezzi"""

    def __init__(self, name, color, l_position):
        self.name = name
        self.color = color
        self.pos = l_position

    def __str__(self):
        return f"{self.name}:l={len(self.pos)}"

    def rotpos(self, xy):
        """
        Data una tupla di cordinate relative (x,y) genera
        una tupla ruotata di 90 gradi

        approfondimento: tecnicamente non si ruotano, si specchiano le coordinate
        """
        r, c = xy
        #if x == 0 or y == 0:
        #    return (-y, -x)
        if r>=0:

            if c>=0:
                return((c, -r))
            else:
                return((c, -r))
        else:
            if c>=0:
                return((c,-r))
            else:
                return((c,-r))


    def rotate(self):
        """ruota un pezzo a dx di 90 gradi prendendo singolarmente la posizione 
        di ogni blocco di un pezzo, restituisce una versione aggiornata della posizione"""
        l_rotpos = list(map(self.rotpos, self.pos))
        self.pos = l_rotpos
        return self

    def unrotate(self):
        """questa funzione ruota un pezzo a sx di 90' facendo 3 rotazioni a dx"""
        self.rotate()
        self.rotate()
        self.rotate()
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


class Pezzi:
    """Factory per i pezzi"""

    def i(self):
        """i: riga gialla"""
        return Pezzo("i", "r", [(0, 1), (0, 0), (0, -1), (0, -2)])

    def z(self):
        """Z: rossa (cambiare)"""
        return Pezzo("z", "g", [(0, -1), (0, 0), (1, 0), (1, 1)])

    def s(self):
        """S: verde"""
        return Pezzo("s", "b", [(0, -1), (0, 0), (-1, 0), (-1, 1)])

    def l(self):
        """L: arancione"""
        return Pezzo(
            "l",
            "o",
            [
                (1, 0),
                (0, 0),
                (2, 0),
                (2, 1),
            ],
        )

    def j(self):
        """Gamma (L rovesciata): blu"""
        return Pezzo("j", "b", [(1, 0), (0, 0), (2, 0), (2, -1)])

    def t(self):
        """T: violetta"""
        return Pezzo("t", "p", [(0, 1), (0, 0), (0, -1), (1, 0)])

    def o(self):
        """Quadrato giallo"""
        return Pezzo("o", "g", [(0, 1), (0, 0), (-1, 0), (-1, 1)])

    def riga_test(self):
        """pezzo speciale test colonne"""
        return Pezzo("-", "r", [(0, -1), (0, 0), (0, 1), (0, 2)])
