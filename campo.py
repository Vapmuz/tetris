"""
Questa classe crea un campo da gioco di dimensioni (r,c).

- il campo è preallocato da subito
- ogni cella contiene un valore di colore
  oppure "" per indicare che è vuota
- le celle possono essere lette via 'val_at'
  ed impostate con 'set_at' passando una tupla (r,c)
- con str() restituisce il campo da gioco
  come una sequenza di righe.
 
"""


class Campo:
    """
    Inizializza un campo da gioco di dimensioni date.
    """

    def __init__(self, size_rows, size_cols):
        self.cols = size_cols
        self.rows = size_rows

        matrix = []
        for i in range(size_rows):
            row = []
            for j in range(size_cols):
                row.append("")
            matrix.append(row)

        self.pf = matrix

    def val_at(self, rc):
        """
        Legge un valore in posizione data (r,c).

        Se r o c sono oltre il valore massimo,
        scoppia con un errore Index Out of Bounds        
        """
        r, c = rc
        return self.pf[r][c]

    def set_at(self, rc, v):
        """
        Scrive un valore v in posizione data
        """
        r, c = rc
        self.pf[r][c] = v

    def __str__(self):
        """
        Stampa tutto il campo come un insieme di righe, separate dal pipe.

        Nelle celle vuote mette "," mentre nelle altre l'iniziale del colore.

        """
        s = ""
        for r in range(self.rows):
            for c in range(self.cols):
                s += self.printable_val_at((r, c))
            s += "|"
        return s

    def printable_val_at(self, rc):
        """Restituisce un solo carattere stampabile per ciascuna posizione"""
        v = self.val_at(rc)
        if v == "":
            return ","
        return v[0]
