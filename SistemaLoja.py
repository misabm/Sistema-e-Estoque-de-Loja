def sistema_loja():
    while True:
        print("\n=== SISTEMA DA LOJA ===")
        print("1 - Consultar produto")
        print("2 - Calcular total")
        print("3 - Calcular troco")
        print("0 - Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Função consultar produto")

        elif opcao == "2":
            print("Função calcular total")

        elif opcao == "3":
            print("Função calcular troco")

        elif opcao == "0":
            print("Voltando ao menu principal...")
            break

        else:
            print("Opção inválida!")