from .estoque import produtos
from .operacoes import (
    aplicar_desconto,
    calcular_frete,
    calcular_imposto,
    calcular_parcelamento,
    calcular_total,
    calcular_troco,
    consultar_produto,
    validar_cpf_cliente,
)

def listar_produtos_disponiveis():
    disponiveis = {}
    for nome, dados in produtos.items():
        if dados["preco"] is not None and dados["quantidade"] > 0:
            disponiveis[nome] = dados
    return disponiveis

def consultar_produto_menu():
    nome = input("Digite o nome do produto: ")
    produto = consultar_produto(produtos, nome)

    if produto is None:
        print("Produto não encontrado.")
        return

    preco = produto["preco"]
    if preco is None:
        preco_texto = "Preço não informado"
    else:
        preco_texto = f"R$ {preco:.2f}"

    print(f"Produto: {nome.strip().title()}")
    print(f"Preço: {preco_texto}")
    print(f"Quantidade: {produto['quantidade']}")

def aplicar_desconto_menu():
    try:
        total = float(input("Digite o total: "))
        porcentagem = float(input("Digite a porcentagem de desconto: "))
        resultado = aplicar_desconto(total, porcentagem)
        print(f"Valor final com desconto: R$ {resultado:.2f}")
    except Exception as erro:
        print(f"Erro: {erro}")

def calcular_troco_menu():
    try:
        total = float(input("Digite o total da compra: "))
        valor_pago = float(input("Digite o valor pago: "))
        troco = calcular_troco(valor_pago, total)
        print(f"Troco: R$ {troco:.2f}")
    except Exception as erro:
        print(f"Erro: {erro}")

def calcular_imposto_menu():
    try:
        total = float(input("Digite o valor total: "))
        taxa_texto = input("Digite a taxa de imposto ou pressione Enter para 10%: ").strip()

        if taxa_texto == "":
            imposto = calcular_imposto(total)
        else:
            taxa = float(taxa_texto) / 100
            imposto = calcular_imposto(total, taxa)

        print(f"Imposto: R$ {imposto:.2f}")
    except Exception as erro:
        print(f"Erro: {erro}")

def calcular_frete_menu():
    try:
        total = float(input("Digite o valor total: "))
        frete = calcular_frete(total)
        print(f"Frete: R$ {frete:.2f}")
    except Exception as erro:
        print(f"Erro: {erro}")

def validar_cpf_menu():
    cpf = input("Digite o CPF: ")
    if validar_cpf_cliente(cpf):
        print("CPF válido.")
    else:
        print("CPF inválido.")

def calcular_total_menu():
    try:
        quantidade_itens = int(input("Quantos itens deseja calcular? "))
        itens = []

        for i in range(quantidade_itens):
            print(f"Item {i + 1}")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            itens.append({"preco": preco, "quantidade": quantidade})

        total = calcular_total(itens)
        print(f"Total calculado: R$ {total:.2f}")
    except Exception as erro:
        print(f"Erro: {erro}")

def calcular_parcelamento_menu():
    try:
        total = float(input("Digite o total da compra: "))
        parcelas = int(input("Digite a quantidade de parcelas: "))
        valor_parcela = calcular_parcelamento(total, parcelas)
        print(f"{parcelas}x de R$ {valor_parcela:.2f}")
    except Exception as erro:
        print(f"Erro: {erro}")

def registrar_compra():
    disponiveis = listar_produtos_disponiveis()

    if not disponiveis:
        print("Não há produtos disponíveis para venda.")
        return

    print("\nProdutos disponíveis:")
    for nome, dados in disponiveis.items():
        print(f"- {nome} | R$ {dados['preco']:.2f} | Estoque: {dados['quantidade']}")

    carrinho = []

    while True:
        nome = input("\nDigite o nome do produto (Enter para finalizar): ").strip()
        if nome == "":
            break

        produto = consultar_produto(produtos, nome)

        if produto is None or produto["preco"] is None or produto["quantidade"] <= 0:
            print("Produto não encontrado ou indisponível.")
            continue

        try:
            quantidade = int(input("Digite a quantidade: "))
        except ValueError:
            print("Quantidade inválida.")
            continue

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            continue

        if quantidade > produto["quantidade"]:
            print(f"Estoque insuficiente. Disponível: {produto['quantidade']}")
            continue

        carrinho.append(
            {
                "nome": nome.strip().title(),
                "preco": produto["preco"],
                "quantidade": quantidade,
            }
        )

    if not carrinho:
        print("Nenhum item foi adicionado ao carrinho.")
        return

    subtotal = calcular_total(carrinho)
    print(f"\nSubtotal: R$ {subtotal:.2f}")

    try:
        desconto = float(input("Digite a porcentagem de desconto (0 para nenhum): "))
        subtotal = aplicar_desconto(subtotal, desconto)
    except Exception:
        print("Desconto inválido. Seguindo sem desconto.")

    imposto = calcular_imposto(subtotal)
    frete = calcular_frete(subtotal)
    total_final = round(subtotal + imposto + frete, 2)

    print(f"Total com desconto: R$ {subtotal:.2f}")
    print(f"Imposto: R$ {imposto:.2f}")
    print(f"Frete: R$ {frete:.2f}")
    print(f"Total final: R$ {total_final:.2f}")

    cpf_opcao = input("Deseja colocar CPF na nota? (s/n): ").strip().lower()
    if cpf_opcao == "s":
        cpf = input("Digite o CPF: ")
        if validar_cpf_cliente(cpf):
            print("CPF válido.")
        else:
            print("CPF inválido.")

    forma = input("Deseja parcelar? (s/n): ").strip().lower()

    if forma == "s":
        try:
            parcelas = int(input("Digite a quantidade de parcelas: "))
            valor_parcela = calcular_parcelamento(total_final, parcelas)
            print(f"{parcelas}x de R$ {valor_parcela:.2f}")
        except Exception as erro:
            print(f"Erro no parcelamento: {erro}")
    else:
        try:
            valor_pago = float(input("Digite o valor pago: "))
            troco = calcular_troco(valor_pago, total_final)
            print(f"Troco: R$ {troco:.2f}")
        except Exception as erro:
            print(f"Erro no pagamento: {erro}")
            return

    for item in carrinho:
        produtos[item["nome"]]["quantidade"] -= item["quantidade"]

    print("Compra finalizada com sucesso.")

def sistema_loja():
    while True:
        print("\n==== SISTEMA DA LOJA ====")
        print("1 - Consultar produto")
        print("2 - Aplicar desconto")
        print("3 - Calcular troco")
        print("4 - Calcular imposto")
        print("5 - Calcular frete")
        print("6 - Validar CPF")
        print("7 - Calcular total")
        print("8 - Calcular parcelamento")
        print("9 - Registrar compra")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            consultar_produto_menu()
        elif opcao == "2":
            aplicar_desconto_menu()
        elif opcao == "3":
            calcular_troco_menu()
        elif opcao == "4":
            calcular_imposto_menu()
        elif opcao == "5":
            calcular_frete_menu()
        elif opcao == "6":
            validar_cpf_menu()
        elif opcao == "7":
            calcular_total_menu()
        elif opcao == "8":
            calcular_parcelamento_menu()
        elif opcao == "9":
            registrar_compra()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")