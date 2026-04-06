from Estoque import produtos
from calcularTotal import calcular_total
from calcularParcelamento import calcular_parcelamento


def listar_produtos_disponiveis():
    disponiveis = {}

    for nome, dados in produtos.items():
        if dados["preco"] is not None and dados["quantidade"] > 0:
            disponiveis[nome] = dados

    if not disponiveis:
        print("Nenhum produto disponivel para venda.")
        return {}

    print("\nProdutos disponiveis:")
    for nome, dados in disponiveis.items():
        print(f"- {nome} | R$ {dados['preco']:.2f} | Estoque: {dados['quantidade']}")

    return disponiveis


def sistema_loja():
    print("\n=== SISTEMA DA LOJA ===")

    if not produtos:
        print("Nenhum produto disponivel para venda.")
        input("Pressione Enter para voltar...")
        return

    disponiveis = listar_produtos_disponiveis()
    if not disponiveis:
        input("\nPressione Enter para voltar...")
        return

    carrinho = []

    while True:
        nome = input("\nDigite o nome do produto (ou Enter para finalizar): ").strip().title()

        if nome == "":
            break

        if nome not in disponiveis:
            print("Produto nao encontrado ou indisponivel.")
            continue

        try:
            quantidade = int(input("Digite a quantidade: "))
            if quantidade <= 0:
                print("A quantidade deve ser maior que zero.")
                continue
        except ValueError:
            print("Quantidade invalida.")
            continue

        estoque_disponivel = disponiveis[nome]["quantidade"]
        if quantidade > estoque_disponivel:
            print(f"Estoque insuficiente. Disponivel: {estoque_disponivel}")
            continue

        carrinho.append(
            {
                "nome": nome,
                "preco": disponiveis[nome]["preco"],
                "quantidade": quantidade,
            }
        )

    if not carrinho:
        print("Nenhum item foi selecionado.")
        input("\nPressione Enter para voltar...")
        return

    total = calcular_total(carrinho)
    print(f"\nTotal da compra: R$ {total:.2f}")

    resposta = input("Deseja parcelar? (s/n): ").strip().lower()
    if resposta == "s":
        try:
            parcelas = int(input("Digite o numero de parcelas: "))
            valor_parcela = calcular_parcelamento(total, parcelas)
            print(f"{parcelas}x de R$ {valor_parcela:.2f}")
        except ValueError:
            print("Numero de parcelas invalido.")

    input("\nPressione Enter para voltar...")
