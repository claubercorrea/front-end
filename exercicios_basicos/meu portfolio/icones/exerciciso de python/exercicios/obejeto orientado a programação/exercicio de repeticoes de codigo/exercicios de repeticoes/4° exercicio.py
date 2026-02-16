# Agregação
class Cliente:
    def __init__(self,nome,endereco,tipo):
      self._tipo = tipo
      self._nome = nome
      self._endereco = endereco
    def imprime (self):
      print('Cliente:', self._nome, '('+self._tipo+')','\nEndereco ', self._endereco)


# ------------------------------------
# Atributos e métodos de classe
class conta:
    _quant= 0
    @classmethod
    def adiciona_conta(cls):
       cls._quant +=1
    @classmethod
    def quantidade(cls):
       return cls._quant
    # print('----------------------')
    # -----------------------------------------------------------------
    # Agregação
    def __init__(self,numero,cliente):
        self.adiciona_conta()
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0.0

    def imprime (self):
       print('Conta:', str(self._numero),'\nSaldo: ', str(self._saldo))
# ------------------------------------------------------------------------
       self._cliente.imprime()
    def deposita(self, valor):
        self._saldo+= valor
    def saldo(self):
        return self._saldo
    
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
    # ---------------------------------------
    # Agregação
cliente = Cliente('Ana', 'Rua um')
conta1 = conta(1111, cliente)
cliente = Cliente('Loja X ', 'Praça central')
conta2= conta(22222, cliente)
conta1.deposita(500.0)
conta1.transferir(conta2,100.00)
conta1.imprime()
print()
conta2.imprime()

# ---------------------------