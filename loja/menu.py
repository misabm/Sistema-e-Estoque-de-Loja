from .estoque import sistema_estoque
from .loja import sistema_loja


def menu_principal() -> None:
    """Menu principal do sistema."""
    while True:
        print("\n==== MENU PRINCIPAL ====")
        print("1 - Sistema da Loja")
        print("2 - Sistema de Estoque")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            sistema_loja()
        elif opcao == "2":
            sistema_estoque()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu_principal()