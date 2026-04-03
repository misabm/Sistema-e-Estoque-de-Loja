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
        produtos[nome] = {"preco": None, "quantidade": 0}
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

    produtos[nome]["preco"] = preco
    print(f"Preço do produto '{nome}' atualizado com sucesso!")


def adicionar_unidade_produto():
    print("\n=== Adicionar Unidade ao Produto ===")
    nome = input("Digite o nome do produto: ").strip().title()

    if nome not in produtos:
        print("Esse produto não existe no estoque.")
        return

    try:
        quantidade = int(input("Digite a quantidade: "))
        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            return
    except ValueError:
        print("Quantidade inválida.")
        return

    produtos[nome]["quantidade"] += quantidade
    print(f"{quantidade} unidade(s) adicionada(s) ao produto '{nome}'.")


def listar_produtos():
    print("\n=== Produtos no Estoque ===")

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for nome, dados in produtos.items():
        preco = dados["preco"]
        quantidade = dados["quantidade"]

        if preco is None:
            preco_texto = "Preço não informado"
        else:
            preco_texto = f"R$ {preco:.2f}"

        print(f"- {nome} | {preco_texto} | Quantidade: {quantidade}")

def remover_produto():
    print("\n=== Remover Produto ===")
    nome = input("Digite o nome do produto que deseja remover: ").strip().title()

    if nome in produtos:
        # O comando 'del' remove a chave e os valores associados
        del produtos[nome]
        print(f"Produto '{nome}' removido com sucesso do estoque!")
    else:
        print(f"Erro: O produto '{nome}' não foi encontrado.")

def atualizar_quantidade():
    print("\n=== Atualizar Quantidade (Sobrescrever) ===")
    nome = input("Digite o nome do produto: ").strip().title()
    if nome not in produtos:
        print("Erro: Produto não encontrado.")
        return
    try:
        nova_qtd = int(input(f"Digite a nova quantidade real para '{nome}': "))
        if nova_qtd < 0:
            print("A quantidade não pode ser negativa.")
            return
        produtos[nome]["quantidade"] = nova_qtd
        print(f"Quantidade de '{nome}' atualizada para {nova_qtd} unidades.")
    except ValueError:
        print("Erro: Digite um número inteiro válido.")

def calcular_total_estoque():
    print("\n=== Valor Total do Estoque ===")

    total = 0

    for dados in produtos.values():
        if dados["preco"] is not None:
            total += dados["preco"] * dados["quantidade"]

    print(f"Valor total do estoque: R$ {total:.2f}")


def gerar_alerta_estoque_baixo():
    limite = 5

    for produto, dados in produtos.items():
        if dados["quantidade"] < limite:
            print(f"⚠ ALERTA: {produto} com {dados['quantidade']} unidade(s)")


def sistema_estoque():
    while True:
        gerar_alerta_estoque_baixo()

        print("\n==== SISTEMA DE ESTOQUE ====")
        print("1 - Adicionar Produto")
        print("2 - Adicionar Preço do Produto")
        print("3 - Adicionar Unidade ao Produto")
        print("4 - Listar Produtos")
        print("5 - Calcular Total do Estoque")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            adicionar_preco_produto()
        elif opcao == "3":
            adicionar_unidade_produto()
        elif opcao == "4":
            atualizar_quantidade()
        elif opcao == "5":
            remover_produto()
        elif opcao == "6":
            listar_produtos()
        elif opcao == "7":
            calcular_total_estoque()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")