from absztrakt_szoba import Szoba
from datetime import datetime

class Foglalas:
    def __init__(self, szoba: Szoba, datum: datetime):
        self.datum = datum
        self.szoba = szoba        

    def __str__(self):
        return f"Foglalás: {self.szoba} - Időpont: {self.datum.date()}"
    
    def __eq__(self, o: object) -> bool:
        # A dátumnak csak a napja számít, az időpont nem
        return self.datum.date() == o.datum.date() and self.szoba == o.szoba
    
    