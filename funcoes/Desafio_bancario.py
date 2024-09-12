menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

valor_conta = 0.0;
LIMITE_SAQUE = 3;

while True:
    opcao = input(menu);

    if opcao == "d":
        print("DEPÓSITO");
        v = input("Digite a quantidade que deseja depositar: ");
        valor = float(v);
        while not v.isdigit():
            print("DIGITE UM VALOR VÁLIDO!");
            v = input("\nDigite a quantidade que deseja depositar: ");
            if v.isdigit():
                break;

        print(f"\nDEPÓSITO DE R${valor} REALIZADO COM SUCESSO!");
        valor_conta += valor;
        print(f"VALOR EM CONTA: {valor_conta}")
            
    elif opcao == "s":
        print("SACAR");
    elif opcao == "e":
        print("EXTRATO");
    elif opcao == "q":
        print("\nOBRIGADO POR USAR NOSSO SISTEMA!");
        break;
    else:
        print("\nOPÇÃO INVÁLIDA, TENTE NOVAMENTE!")