"""
Questa classe rcea un campo da gioco di dimensioni (r,c).

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
    RICORDARSI Y*X (colonne per righe non righe per colonne)
    """

    def __init__(self, size_rows, size_cols):
        self.cols = size_cols
        self.rows = size_rows

        matrix = []
        for _ in range(size_rows):
            row = []
            for _ in range(size_cols):
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
        Srcive un valore v in posizione data
        """
        r, c = rc
        self.pf[r][c] = v

    def valid_pos(self, rc):
        """Controlla se una posizione è valida, ovvero compresa
        tra (0,0) e (rows-1, cols-1)
        """
        r, c = rc
        if (r < 0) or (r >= self.rows):
            return False
        if (c < 0) or (c >= self.cols):
            return False
        return True

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

    def space_available(self, l_abs_pos, color):
        """controlla che per tutte le coordinate passate in l_abs_pos saino valide
        e che il pixel abbia il colore richiesto (se vuoto il colore è "").
        ritorna False se non rispetta i rcitieri per almeno una coordinata,
        True se tzutte le coordinate li rispettano"""
        for rc_p in l_abs_pos:
            if self.valid_pos(rc_p) is False:
                return False
            if self.val_at(rc_p) != color:
                return False
        return True

    def plot_at(self, rc, pezzo):
        """Posiziona un pezzo nel campo avente il centro in (r,c).

        Ritorna true se il disegno ha avuto successo (tutte le celle erano
        valide e vuote) e false se erano occupate o inesistenti.
        """
        abs_pos = pezzo.positionate_piece(rc)
        if self.space_available(abs_pos, "") is False:
            return False
        for rc_p in abs_pos:
            self.set_at(rc_p, pezzo.color)
        return True

    def unplot_at(self, rc, pezzo):
        """
        rimuovi il pezzo inserito trovando la sua abs_pos e sostituendo nelle celle con dei ","
        ritorna: true se la cancellazione ha avuto successo
        false se non ha vuto successo ovvero: i pixel non erano dewl colore richiesto oppure
        erano fuori dal campo di gioco.
        """
        abs_pos = pezzo.positionate_piece(rc)
        if self.space_available(abs_pos, pezzo.color) is False:
            return False
        for rc_p in abs_pos:
            self.set_at(rc_p, "")
        return True

    def is_all_empty(self):
        """controlla che tutte le celle del campo siano vuote
        restituisce False se almeno una cella è piena
        restituisce True se tutte so vuote"""
        for r in range(self.rows):
            for c in range(self.cols):
                if self.val_at((r, c)) != "":
                    return False
        return True

    def is_fulline(self, lrow):
        """
        controlla se in una lista è presente il carattere ""
        se lo trova ritorna False, se non lo trova ritorna True
        """
        if "" in lrow:
            return False
        else:
            return True

    def fullline_at(self):
        """
        Questa funzione controlla se ci sono delle linee piene
        se ne trova una ritorna una tupla contenente la colonna, 
        se invece non ne trova nessuna ritorna False
        """
        rows_full = []
        for r in range(self.rows):
            lst = []
            for c in range(self.cols):
                rc = (r, c)
                lst.append(self.val_at(rc))
            if self.is_fulline(lst):
                rows_full.append(r)
        return rows_full
