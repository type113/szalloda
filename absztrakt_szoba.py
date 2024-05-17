from abc import ABC, abstractmethod

class Szoba(ABC):
    def __init__(self, ar):
        self.ar = ar
        
    
    @abstractmethod
    def jellemzes(self):
        pass
