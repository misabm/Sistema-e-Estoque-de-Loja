from Estoque import produtos


def sistema_loja():
    print("\n=== SISTEMA DA LOJA ===")

    if not produtos:
        print("Nenhum produto disponível para venda.")
        input("Pressione Enter para voltar...")
        return

    print("\nProdutos disponíveis:")

    for nome, dados in produtos.items():
        if dados["preco"] is not None and dados["quantidade"] > 0:
            print(f"- {nome} | R$ {dados['preco']:.2f} | Estoque: {dados['quantidade']}")

    input("\nPressione Enter para voltar...")