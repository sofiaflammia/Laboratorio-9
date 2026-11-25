class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self._saldo += monto
        else:
            print("Monto inválido")

    def retirar(self, monto):
        if 0 < monto <= self._saldo:
            self._saldo -= monto
            return True
        print("Fondos insuficientes")
        return False

    def obtener_saldo(self):
        return self._saldo

    def transferir(self, destino, monto):
        if monto <= 0:
            print("Monto inválido")
            return False
        if self.retirar(monto):
            destino.depositar(monto)
            return True
        return False