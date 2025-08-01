# Crea un campo da gioco di dimensioni (r,c).
# 
# - il campo è preallocato da subito
# - ogni cella contiene un valore di colore 
#.  oppure "" per indicare che è vuota
# - le celle possono esssere lette via 'val_at'
#.  ed impostate con 'set_at' passando una tupla (r,c)
# - con str() restituisce il campo da gioco
#.  come una sequenza di righe.
class Campo:
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
        
    
    # Legge un valore in posizione data.
    # Se r o c sono oltre il valore massimo,
    # scoppia con un errore Index Out of Bounds
    def val_at(self, rc):
        r, c = rc
        return self.pf[r][c]
    
    # Scrive un valore v in posizione data
    def set_at(self, rc, v):
        r, c = rc
        self.pf[r][c] = v


    # Stampa tutto il campo come un insieme 
    # di righe. 
    # Nelle calle vuote mette "," mentre 
    # nelle altre l'inziale del colore.
    def __str__(self):
        s = ""
        for r in range(self.rows):
            for c in range(self.cols):
                s += self.printable_val_at((r, c))
            s += "\n"
        return s
    
    def printable_val_at(self, rc):
        v = self.val_at(rc)
        if v == "":
            return ","
        else:    
            return v[0]

