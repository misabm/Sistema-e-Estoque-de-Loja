from Estoque import produtos

def calcular_imposto(valor_total, taxa=0.10):
    if not isinstance(valor_total, (int, float)) or valor_total < 0: return 0.0
    return round(valor_total * taxa, 2)

def calcular_frete(valor_total):
    if not valor_total or valor_total <= 0: return 0.0
    if valor_total >= 200: return 0.0
    return 7.50 if valor_total >= 100 else 15.00

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