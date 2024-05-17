from absztrakt_szoba import Szoba

class EgyagyasSzoba(Szoba):
    def __init__(self, klima=False):
        super().__init__(ar=5000)
        self.klima = klima

    def jellemzes(self):
        return f"Egyágyas szoba {'klímával' if self.klima else 'klíma nélkül'} - Ára {self.ar} Ft"
    
    def van_klima(self):
        return self.klima
    
    def __str__(self) -> str:
        return self.jellemzes()
    
    def __eq__(self, o: object) -> bool:
        return type(self) == type(o) and self.klima == o.klima
    
    
class KetagyasSzoba(Szoba):
    def __init__(self, erkely=False):
        super().__init__(ar=8000)
        self.erkely = erkely

    def jellemzes(self):
        return f"Kétágyas szoba {'erkéllyel' if self.erkely else 'erkély nélkül'} - Ára {self.ar} Ft"
    
    def van_erkely(self):
        return self.erkely
    
    def __str__(self) -> str:
        return self.jellemzes()
    
    def __eq__(self, o: object) -> bool:
        return type(self) == type(o) and self.erkely == o.erkely
    