## 1
from abc import ABC, abstractmethod

class Shartnoma(ABC):

    @abstractmethod
    def summa(self):
        pass


class SavdoShartnomasi(Shartnoma):

    def __init__(self, narx, miqdor):
        self.narx = narx
        self.miqdor = miqdor

    def summa(self):
        return self.narx * self.miqdor


s = SavdoShartnomasi(10000, 5)
print("Umumiy summa:", s.summa())




## 2
from abc import ABC, abstractmethod

class Shartnoma(ABC):

    def saqlash(self):
        print("Bazaga saqlandi")

    @abstractmethod
    def imzolash(self):
        pass



## 3
def jarayon(shartnoma):
    shartnoma.imzolash()


class MehnatShartnomasi:
    def imzolash(self):
        print("Mehnat shartnomasi imzolandi")


class IjaraShartnomasi:
    def imzolash(self):
        print("Ijara shartnomasi imzolandi")


jarayon(MehnatShartnomasi())
jarayon(IjaraShartnomasi())



## 4
from abc import ABC, abstractmethod

class Shartnoma(ABC):

    @property
    @abstractmethod
    def turi(self):
        pass


class MehnatShartnomasi(Shartnoma):

    @property
    def turi(self):
        return "Mehnat"



## 5
from abc import ABC, abstractmethod

class Shartnoma(ABC):

    @abstractmethod
    def imzo_tekshir(self):
        pass


class ElektronShartnoma(Shartnoma):

    def imzo_tekshir(self):
        print("Elektron imzo tasdiqlandi")



## 6
from abc import ABC, abstractmethod

class Shartnoma(ABC):

    @abstractmethod
    def tolov(self):
        pass


class OnlineShartnoma(Shartnoma):

    def tolov(self):
        print("Online to'lov amalga oshirildi")


class OfisShartnoma(Shartnoma):

    def tolov(self):
        print("Ofisda naqd to'lov qilindi")
