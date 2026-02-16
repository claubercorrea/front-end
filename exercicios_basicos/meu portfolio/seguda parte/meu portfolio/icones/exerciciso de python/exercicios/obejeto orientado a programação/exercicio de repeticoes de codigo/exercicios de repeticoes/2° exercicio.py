class conta:
    def __init__(self,numero):
        self._numero = numero
        self._saldo = 0.0

    def deposita(self, valor):
        self._saldo+= valor
    def saldo(self):
        return self._saldo
    # -------------------------
    # Encapsulamento
    def sacar(self,valor):
       if self._saldo >= valor:
        self._saldo -= valor
        return True
       return False

    def transferir(self,destino,valor):
       if self.sacar(valor):
          destino.deposita(valor)
          return True
       return False
          
conta1 = conta(22222)
print('conta1', conta1.saldo())
conta1.deposita(1000.00)
print('\nconta1', conta1.saldo())
conta1.sacar(100.00)
print('conta1', conta1.saldo())
conta2 =  conta(33333)
print('\nconta2', conta2.saldo())
conta2.deposita(2000.00)

print('conta2', conta2.saldo())
conta2.sacar(100.00)
print('conta2', conta2.saldo())
# ---------------------------------------
print('\nsaldo apos a tranferencia')
conta1.transferir(conta2, 200.00)
print('conta2', conta2.saldo())
print('conta1', conta1.saldo())
# ---------------------------------------