"""
Restituisce il prossimo pezzo, nella sua posizione base.

- The Random Generator (also known as "random bag" or "7 bag") 
  determines the sequence of tetrominoes during gameplay. 
  One of each of the 7 tetrominoes are shuffled in a "bag", 
  and are dealt out one by one. When the bag is empty, a 
  new one is filled and shuffled.
- Tetrominoes appear on the 21st and 22nd rows of the playfield, 
  centered and rounded to the left when needed. 
  They must start with their flat side down, and move down 
  immediately after appearing.

"""
import random
from pezzo import Pezzi


class Nextup:
    """
    La classe che implementa i prossimi pezzi, caricati una bag alla volta.
    La classe tiene il conto del numero di pezzi prelevati.
    """

    def __init__(self):
        """Genera un oggetto vuoto."""
        self.queue = []
        self.pops = 0

    def __str__(self):
        """Genera: 'Nextup:jlfr(56)' dove
        il valore stringa sono i tipi di pezzi nella coda
        e 56 il numero di pezzi prelevati tramite pop().
        """
        pezzi = ""
        for p in self.queue:
            pezzi += p.name
        return f"Nextup:{pezzi}({self.pops})"

    def fill(self):
        """Aggiunge una bag di elementi alla mia coda."""
        pp = Pezzi()
        bag = [pp.i(), pp.s(), pp.j(), pp.l(), pp.o(), pp.t(), pp.z()]
        random.shuffle(bag)
        for p in bag:
            self.queue.append(p)

    def pop(self):
        """
        Restituisce il primo elemento dalla coda e lo 
        elimina. 

        Se non vi sono pezzi nella coda, ne aggiunge una bag.
        """
        if len(self.queue) == 0:
            self.fill()

        v = self.queue.pop(0)
        self.pops += 1
        return v

    def peek(self, offset):
        """
        Mi restituisce il pezzo alla posizione 'offset' che 
        verrà prelevato in futuro. Il pezzo NON viene pelevato,
        quindi il pezzo '0' è il prossimo, il pezzo '1' quello successivo, 
        e così via.

        Se non vi sono abbastanza pezzi nella coda, li genera fino 
        all'offset richiesto, aggiungendo un certo numero di bags.
        """
        # anche se l'offset è zero, devo fare un refill!
        while len(self.queue) <= offset:
            self.fill()
        return self.queue[offset]
