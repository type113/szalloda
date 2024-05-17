from absztrakt_szoba import Szoba
from foglalas import Foglalas
from szoba import EgyagyasSzoba, KetagyasSzoba
from datetime import datetime
import random

class Szalloda:

    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = {}

    def get_nev(self):
        return self.nev


    def uj_szoba_hozzaadasa(self, szoba: Szoba):
        self.szobak.append(szoba)


    def osszes_szoba_jellemzese(self):
        jellemzesek = []
        for szoba in self.szobak:
            jellemzesek.append(szoba.jellemzes())
        return jellemzesek


    def a_szoba_szabad(self, sajat_szoba, datum: datetime):
        ok = True
        for foglalas in self.foglalasok.values():
            # Ha a szoba és a dátum megegyezik, akkor nem szabad a szoba
            # A dátumnak csak a napja számít, az időpont nem
            if foglalas.szoba == sajat_szoba and foglalas.datum.date() == datum.date():
                ok = False
                break
        if ok:
            return True             
        return False


    def foglalas(self, foglalando_szoba: Szoba, datum: datetime):
        if datum.date() < datetime.now().date():
            return False, "Múltbeli időpontra nem lehet foglalni."
        sajat_lefoglalando_szoba = None
        for sajat_szoba in self.szobak:
            if foglalando_szoba==sajat_szoba and self.a_szoba_szabad(sajat_szoba, datum):
                sajat_lefoglalando_szoba = sajat_szoba
                break
        if not sajat_lefoglalando_szoba:
            for sajat_szoba in self.szobak:
                # Ha nincs klíma vagy erkély nélküli szoba, akkor jó a klímás vagy erkélyes is (mert nem muszály ezeket használni) 
                if (isinstance(foglalando_szoba, EgyagyasSzoba) and not foglalando_szoba.klima) or (isinstance(foglalando_szoba, KetagyasSzoba) and not foglalando_szoba.erkely):
                    if type(foglalando_szoba) == type(sajat_szoba) and self.a_szoba_szabad(sajat_szoba, datum):
                        sajat_lefoglalando_szoba = sajat_szoba
                        break
        if sajat_lefoglalando_szoba:
            foglalas = Foglalas(sajat_lefoglalando_szoba, datum)
            foglalas_szam = random.randint(1000, 9999)
            while foglalas_szam in self.foglalasok:
                foglalas_szam = random.randint(1000, 9999)
            self.foglalasok[foglalas_szam] = foglalas
            return True, foglalas_szam
        else:
            return False, "Nincs szabad szoba a megadott időpontra."


    def foglalas_lemondasa(self, foglalas_szam: int):
        if foglalas_szam in self.foglalasok:
            del self.foglalasok[foglalas_szam]
            return True
        else:
            return False


    def osszes_foglalas_listazasa(self):
        lista = []
        if self.foglalasok:
            for foglalas_szam, foglalas in self.foglalasok.items():
                lista.append((foglalas_szam, foglalas))
        return lista        
