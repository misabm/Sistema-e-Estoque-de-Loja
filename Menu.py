from SistemaLoja import sistema_loja
from Estoque import sistema_estoque


def menu_principal():
    while True:
        print("\n==== MENU PRINCIPAL ====")
        print("1 - Sistema da Loja")
        print("2 - Sistema de Estoque")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sistema_loja()
        elif opcao == "2":
            sistema_estoque()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida!")


menu_principal()