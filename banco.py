git init

git remote add origin https://github.com/MauricioJJPavan/SistemaBancario.git

git add .
git commit -m "Primeira versão do sistema bancário"


class SistemaBancario:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque.")
        elif valor > 500:
            print("Limite máximo de saque diário é de R$ 500.00.")
        elif self.saldo < valor:
            print("Saldo insuficiente para saque.")
        else:
            self.saldo -= valor
            self.saques.append(valor)
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def extrato(self):
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for deposito in self.depositos:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in self.saques:
                print(f"Saque: R$ {saque:.2f}")
            print(f"Saldo atual: R$ {self.saldo:.2f}")


def main():
    sistema = SistemaBancario()

    while True:
        print("\nOpções:")
        print("0 - Sair")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Extrato")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 0:
            print("Saindo do sistema.")
            break
        elif opcao == 1:
            valor = float(input("Digite o valor para depósito: "))
            sistema.depositar(valor)
        elif opcao == 2:
            valor = float(input("Digite o valor para saque: "))
            sistema.sacar(valor)
        elif opcao == 3:
            sistema.extrato()
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()


git push -u origin master
