from enum import Enum

class Time(Enum):
    T0645 = 0
    T0815 = 1
    T0945 = 2
    T1115 = 3
    T1245 = 4
    T1415 = 5
    T1545 = 6
    T1715 = 7
    T1845 = 8
    T2015 = 9


    def __lt__(self, objeto):
        return((self.value) <(objeto.value))
    
    def __gt__(self, objeto):
        return((self.value) > (objeto.value))
    
    def __le__(self, objeto):
        return((self.value) <= (objeto.value))
    
    def __ge__(self, objeto):
        return((self.value) >= (objeto.value))
    
    def __eq__(self, objeto) -> bool:
        return (self.value == objeto.value)  #duda
    
    def __repr__(self) -> str:
        hora = ""
        if self.value == 0:
            hora = "6:45 - 8:15"
        elif self.value == 1:
            hora = "8:15 - 9:45"
        elif self.value == 2:
            hora = "9:45 - 11:15"
        elif self.value == 3:
            hora = "11:15 - 12:45"
        elif self.value == 4:
            hora = "12:45 - 14:15"
        elif self.value == 5:
            hora = "14:15 - 15:45"
        elif self.value == 6:
            hora = "15:45 - 17:15"
        elif self.value == 7:
            hora = "17:15 - 18:45"
        elif self.value == 8:
            hora = "18:45 - 20:15"
        elif self.value == 9:
            hora = "20:15 - 21:45"
        return hora