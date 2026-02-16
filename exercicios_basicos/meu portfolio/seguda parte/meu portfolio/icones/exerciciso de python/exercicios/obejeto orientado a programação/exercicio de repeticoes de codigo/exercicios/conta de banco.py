class Cliente:
    def __init__(self,nome,endereco,tipo):
        self._tipo = tipo
        self._nome =  nome
        self._endereco = endereco
    def imprime(self):
        print('Cliente:',self._nome, ''+self._tipo+'','\nEndereco', self._endereco)
class Conta:
    _quant=0
    @classmethod
    def adiciona_conta(cls):
        cls._quant +=1
    @classmethod
    def quantidade(cls):
        return cls._quant
    
    def __init__(self,numero,cliente):
        self.adiciona_conta()
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0.0
    
    def imprime(self):
        print('Conta:', str(self._numero),
        '\nSaldo: ', str(self._saldo))
    
        self._cliente.imprime()
                
    def depositar(self,valor):
        self._saldo +=valor
    def saldo(self):
        return self._saldo
    def sacar(self,valor):
          if self._saldo >=valor:
            self._saldo -= valor
            return True
          return False
    def transferir(self,destino,valor):
        if self.sacar(valor):
            destino.depositar(valor)
            return True
        return False
    

      
print('-----------conta1-----------')

print('contas criadas', Conta.quantidade())
Cliente1 = Cliente ('Ana Clara', 'Rua um')

conta1 = Conta(1122)
print('conta1', conta1.saldo())  
conta1.depositar(1000)
print('conta1:R$',  conta1.saldo())

conta1.sacar(100.00)    
print('conta1:R$', conta1.saldo())

print('\n----------conta2-------------')
print('contas criadas', Conta.quantidade())
Cliente2 = Cliente('Maria','Rua Dois')
conta2 = Conta(2222)
print('conta2:R$', conta2.saldo())
conta2.depositar(2000.00)
print('conta2:R$', conta2.saldo())
print('imprime a conta 2', conta2.imprime())
print('------------saldo atual---------------------')
conta1.sacar(100.00)
print('conta1:R$', conta1.saldo())
print('------------------conta2-----------------')
conta2.sacar(100.00)
print('saldo da conta2:R$', conta2.saldo())

print('-------------------tranferencia da conta1-------------')

conta1.transferir(conta2,100.00)

print('saldo atual da conta1:R$', conta1.saldo())

print('\nTranferencia da conta2')
conta2.transferir(conta1,200.00)
print('\n---------saldo atual da conta2-----------')
print(' conta2:R$', conta2.saldo())

print('\n-----------------------Saldo atual das duas contas---------------')

print('Saldo atual da conta1: R$', conta1.saldo())

print('\nSaldo atual da conta2:R$', conta2.saldo())

print('\n------------quantidade de contas criadas-----------------------')
print(Conta.quantidade())

