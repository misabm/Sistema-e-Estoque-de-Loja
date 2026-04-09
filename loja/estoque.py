from .operacoes import calcular_total

produtos = {}


def adicionar_produto(produtos_dict: dict, nome: str, preco=None, quantidade: int = 0) -> None:
    """Adiciona um produto ao estoque."""
    if not isinstance(produtos_dict, dict):
        raise TypeError("O estoque deve ser um dicionário.")

    nome = nome.strip().title()

    if nome == "":
        raise ValueError("O nome do produto não pode ser vazio.")
    if nome in produtos_dict:
        raise ValueError("O produto já existe no estoque.")
    if preco is not None and not isinstance(preco, (int, float)):
        raise TypeError("O preço deve ser numérico ou None.")
    if preco is not None and preco < 0:
        raise ValueError("O preço não pode ser negativo.")
    if not isinstance(quantidade, int):
        raise TypeError("A quantidade deve ser inteira.")
    if quantidade < 0:
        raise ValueError("A quantidade não pode ser negativa.")

    produtos_dict[nome] = {"preco": None if preco is None else round(float(preco), 2), "quantidade": quantidade}


def adicionar_preco_produto(produtos_dict: dict, nome: str, preco: float) -> None:
    """Define ou atualiza o preço de um produto existente."""
    nome = nome.strip().title()

    if nome not in produtos_dict:
        raise KeyError("Produto não encontrado.")
    if not isinstance(preco, (int, float)):
        raise TypeError("O preço deve ser numérico.")
    if preco < 0:
        raise ValueError("O preço não pode ser negativo.")

    produtos_dict[nome]["preco"] = round(float(preco), 2)


def atualizar_quantidade(produtos_dict: dict, nome: str, nova_quantidade: int) -> None:
    """Substitui a quantidade de um produto por um novo valor."""
    nome = nome.strip().title()

    if nome not in produtos_dict:
        raise KeyError("Produto não encontrado.")
    if not isinstance(nova_quantidade, int):
        raise TypeError("A quantidade deve ser inteira.")
    if nova_quantidade < 0:
        raise ValueError("A quantidade não pode ser negativa.")

    produtos_dict[nome]["quantidade"] = nova_quantidade


def remover_produto(produtos_dict: dict, nome: str) -> None:
    """Remove um produto do estoque."""
    nome = nome.strip().title()

    if nome not in produtos_dict:
        raise KeyError("Produto não encontrado.")

    del produtos_dict[nome]


def calcular_total_estoque(produtos_dict: dict) -> float:
    """Calcula o valor total de todos os itens do estoque."""
    itens = []

    for dados in produtos_dict.values():
        if dados["preco"] is not None:
            itens.append({"preco": dados["preco"], "quantidade": dados["quantidade"]})

    if not itens:
        return 0.0

    return calcular_total(itens)


def gerar_alerta_estoque_baixo(produtos_dict: dict, limite: int = 5) -> list:
    """Retorna uma lista de produtos com quantidade abaixo do limite."""
    if not isinstance(limite, int):
        raise TypeError("O limite deve ser inteiro.")
    if limite < 0:
        raise ValueError("O limite não pode ser negativo.")

    alertas = []

    for nome, dados in produtos_dict.items():
        if dados["quantidade"] < limite:
            alertas.append(nome)

    return alertas


def listar_produtos(produtos_dict: dict) -> list:
    """Retorna uma lista de textos formatados com os produtos do estoque."""
    lista = []

    for nome, dados in produtos_dict.items():
        preco = dados["preco"]
        preco_texto = "Preço não informado" if preco is None else f"R$ {preco:.2f}"
        lista.append(f"{nome} | {preco_texto} | Quantidade: {dados['quantidade']}")

    return lista


def sistema_estoque() -> None:
    """Menu interativo do estoque."""
    while True:
        print("\n==== SISTEMA DE ESTOQUE ====")
        print("1 - Adicionar produto")
        print("2 - Adicionar preço ao produto")
        print("3 - Atualizar quantidade")
        print("4 - Remover produto")
        print("5 - Listar produtos")
        print("6 - Calcular total do estoque")
        print("7 - Gerar alerta de estoque baixo")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Digite o nome do produto: ")
            try:
                adicionar_produto(produtos, nome)
                print("Produto adicionado com sucesso.")
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "2":
            nome = input("Digite o nome do produto: ")
            try:
                preco = float(input("Digite o preço do produto: "))
                adicionar_preco_produto(produtos, nome, preco)
                print("Preço atualizado com sucesso.")
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "3":
            nome = input("Digite o nome do produto: ")
            try:
                nova_quantidade = int(input("Digite a nova quantidade: "))
                atualizar_quantidade(produtos, nome, nova_quantidade)
                print("Quantidade atualizada com sucesso.")
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "4":
            nome = input("Digite o nome do produto: ")
            try:
                remover_produto(produtos, nome)
                print("Produto removido com sucesso.")
            except Exception as erro:
                print(f"Erro: {erro}")

        elif opcao == "5":
            lista = listar_produtos(produtos)
            if not lista:
                print("Nenhum produto cadastrado.")
            else:
                for linha in lista:
                    print(linha)

        elif opcao == "6":
            total = calcular_total_estoque(produtos)
            print(f"Valor total do estoque: R$ {total:.2f}")

        elif opcao == "7":
            alertas = gerar_alerta_estoque_baixo(produtos)
            if not alertas:
                print("Nenhum produto com estoque baixo.")
            else:
                print("Produtos com estoque baixo:")
                for nome in alertas:
                    print(nome)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")