menu = """
[d] Depositar

[s] Sacar

[e] Extrato

[q] Sair
=> """

saldo = 0.0
cont = 0.0
LIMITE_SAQUE = 3
extrato = ""

def verificador(v, *, funcao):
    while not v.isdigit():
        print("DIGITE UM VALOR VÁLIDO!")
        v = input(f"\nDigite a quantidade que deseja {funcao}: ")
        if v.isdigit():
            break


def deposito(n):
    global saldo
    global extrato
    saldo += n
    print(f"\nDEPÓSITO DE R${n:.2f} REALIZADO COM SUCESSO!")
    print(f"VALOR EM CONTA: {saldo:.2f}")
    extrato += f"\nDepósito de R${n:.2f}"


def saque(n):
    global saldo
    global extrato
    saldo -= n
    print(f"\nSAQUE DE R${n:.2f} REALIZADO COM SUCESSO!")
    print(f"VALOR EM CONTA: {saldo:.2f}")
    extrato += f"\nSaque de R${n:.2f}"


while True:
    opcao = input(menu).upper()
    if opcao == "D":
        print("DEPÓSITO")
        v = input("Digite a quantidade que deseja depositar: ")
        verificador(v, funcao="depositar")
        n = float(v)
        deposito(n)

    elif opcao == "S":
        cont += 1

        if cont > LIMITE_SAQUE:
            print(f"\nSÓ É POSSÍVEL REALIZAR {LIMITE_SAQUE} DE SAQUES POR DIA!")
        else:
            print("SACAR")
            v = input("Digite a quantidade que deseja sacar: ")
            verificador(v, funcao="sacar")
            n = float(v)
            while n > saldo:
                print(
                    f"\nNÃO É POSSÍVEL SACAR ESTA QUANTIDADE! SEU SALDO ATUAL É DE R${saldo:.2f}"
                )
                v = input("Digite a quantidade que deseja sacar: ")
                n = float(v)
                if n <= saldo:
                    break
            while n > 500:
                print(
                    f"\nNÃO É POSSÍVEL SACAR MAIS QUE R$500! SELECIONE OUTRA QUANTIDADE."
                )
                v = input("Digite a quantidade que deseja sacar: ")
                n = float(v)
                if n <= 500:
                    break
            saque(n)

    elif opcao == "E":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "Q":
        print("\nOBRIGADO POR USAR NOSSO SISTEMA!")
        break
    else:
        print("\nOPÇÃO INVÁLIDA, TENTE NOVAMENTE!")