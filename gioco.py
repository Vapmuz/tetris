"""
La struttura del gioco.

può essere lanciato su stdout via:
    python3 gioco.py

"""
import textwrap

from campo import Campo
from nextup import Nextup


class Gioco:
    """
    Fa girare il gioco, uno step per volta.
    """

    def __init__(self):
        """Genera un oggetto vuoto."""
        self.playing = True
        self.iterations = 0
        self.score = 0
        self.lines = 0
        self.pf = Campo(20, 10)
        self.nextup = Nextup()
        self.pezzo = self.nextup.pop()
        # centrato in qualche modo
        self.r = 2
        self.c = 4

    def __str__(self):
        """
        Stampa lo stato del gioco.
        """
        return textwrap.dedent(f"""
        Gioco attivo? {self.playing} (iter #{self.iterations})
        - score: {self.score} / lines: {self.lines} 
        - pezzi: {self.nextup.pops}
        - nextup: {self.nextup}
        - pezzo attivo: {self.pezzo} ({self.r},{self.c})
        -------------------------------------------------------

        """ + self.pf.as_stdout())

    def command(self, cmd):
        """
        Processa un comando che può essere:
        - l: freccia a sx
        - r: freccia a dx
        - x: ruota

        Altri comandi sono ignorati e non hanno effetto.
        Processa tutto il ciclo del gioco.

        - comando (se possibile)
        - sposta in giù
        - controlla collisione
        - controlla righe complete
        - aggiorna hiscore
        - determina se gioco finito
        """

        self.pf.unplot_at((self.r, self.c), self.pezzo)

        if cmd == "l":
            self.c += -1
        elif cmd == "r":
            self.c += 1
        elif cmd == "x":
            self.pezzo.rotate()

        self.r += 1

        self.pf.plot_at((self.r, self.c), self.pezzo)

        return self

    def debugloop(self):
        """Una versione minima del gioco che funziona a tastiera."""
        while self.playing is True:
            print(str(self))
            cmd = input("l r x:")
            if cmd in ['l', 'r', 'x']:
                self.command(cmd)
            else:
                print("Comando sconosciuto")
                self.command("")
            self.iterations += 1


# Questo blocco si esegue solo quando il file viene eseguito direttamente
if __name__ == "__main__":
    g = Gioco()
    g.debugloop()
