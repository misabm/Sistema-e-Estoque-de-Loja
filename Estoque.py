produtos = {}

def adicionar_produto():
    print("\n=== Adicionar Produto ===")
    nome = input("Digite o nome do produto: ").strip()

    if nome == "":
        print("O nome do produto não pode ser vazio.")
        return

    nome = nome.title()

    if nome in produtos:
        print("Esse produto já existe no estoque.")
    else:
        produtos[nome] = None
        print(f"Produto '{nome}' adicionado com sucesso!")


def adicionar_preco_produto():
    print("\n=== Adicionar Preço do Produto ===")
    nome = input("Digite o nome do produto: ").strip().title()

    if nome not in produtos:
        print("Esse produto não existe no estoque.")
        return

    try:
        preco = float(input("Digite o preço do produto: "))
        if preco < 0:
            print("O preço não pode ser negativo.")
            return
    except ValueError:
        print("Preço inválido.")
        return

    produtos[nome] = preco
    print(f"Preço do produto '{nome}' atualizado com sucesso!")


def listar_produtos():
    print("\n=== Produtos no Estoque ===")

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for nome, preco in produtos.items():
        if preco is None:
            print(f"- {nome} | Preço não informado")
        else:
            print(f"- {nome} | R$ {preco:.2f}")

def calcular_total_estoque():
    print("\n=== Valor Total do Estoque ===")

    total = 0

    for produto, dados in produtos.items():
        preco = dados["preco"]
        quantidade = dados["quantidade"]

        total += preco * quantidade

    print(f"Valor total do estoque: R$ {total:.2f}")

def gerar_alerta_estoque_baixo():
    limite = 5

    for produto, dados in produtos.items():
        if dados["quantidade"] < limite:
            print(f"⚠ ALERTA: {produto} está com estoque baixo ({dados['quantidade']} unidades)")


def sistema_estoque():
    gerar_alerta_estoque_baixo()
    
    while True:
        print("\n==== SISTEMA DE ESTOQUE ====")
        print("1 - Adicionar Produto")
        print("2 - Adicionar Preço do Produto")
        print("3 - Listar Produtos")
        print("4 - Calcular Total do Estoque")
        print("0 - Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            adicionar_preco_produto()
        elif opcao == "3":
            listar_produtos()
        elif opcao == "4":
            calcular_total_estoque()
        elif opcao == "0":
            print("Voltando ao menu principal...")
            break
        
        else:
            print("Opção inválida!")