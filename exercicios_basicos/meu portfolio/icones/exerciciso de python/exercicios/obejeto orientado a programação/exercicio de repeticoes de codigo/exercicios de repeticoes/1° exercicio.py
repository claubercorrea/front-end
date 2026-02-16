# classe
class Conta:
    def __init__(self,numero):
        self._numero = numero
        self._saldo = 0.0
    def depositar(self,valor):
        self._saldo+=valor
    def saldo (self):
        return self._saldo
conta1 =Conta(1234)
print('conta1:', conta1.saldo())
conta2= Conta(3333)
print('conta2', conta2.saldo())

