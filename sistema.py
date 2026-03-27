def sistema_loja():
    print("Você entrou no Sistema da Loja")
    # aqui depois vão ficar as funções da loja
    pass


def sistema_estoque():
    print("Você entrou no Sistema de Estoque")
    # aqui depois vão ficar as funções do estoque
    pass


def menu_principal():
    print("==== MENU PRINCIPAL ====")
    print("1 - Sistema da Loja")
    print("2 - Estoque")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        sistema_loja()
    elif opcao == "2":
        sistema_estoque()
    else:
        print("Opção inválida!")


menu_principal()