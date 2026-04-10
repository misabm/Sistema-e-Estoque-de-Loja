from typing import Iterable


def aplicar_desconto(total: float, porcentagem: float) -> float:
    """
    Aplica um desconto em cima de um valor total.

    Recebe o total da compra e a porcentagem de desconto.
    Retorna o valor final já com o desconto aplicado.
    """
    if not isinstance(total, (int, float)):
        raise TypeError("O total deve ser numérico.")
    if not isinstance(porcentagem, (int, float)):
        raise TypeError("A porcentagem deve ser numérica.")
    if total < 0:
        raise ValueError("O total não pode ser negativo.")
    if porcentagem < 0 or porcentagem > 100:
        raise ValueError("A porcentagem deve estar entre 0 e 100.")
    return round(total * (1 - porcentagem / 100), 2)


def calcular_troco(valor_pago: float, total: float) -> float:
    """
    Calcula o troco de uma compra.

    Recebe o valor pago pelo cliente e o total da compra.
    Retorna quanto deve ser devolvido de troco.
    """
    if not isinstance(valor_pago, (int, float)):
        raise TypeError("O valor pago deve ser numérico.")
    if not isinstance(total, (int, float)):
        raise TypeError("O total deve ser numérico.")
    if valor_pago < 0 or total < 0:
        raise ValueError("Os valores não podem ser negativos.")
    if valor_pago < total:
        raise ValueError("O valor pago é insuficiente.")
    return round(valor_pago - total, 2)


def calcular_imposto(valor_total: float, taxa: float = 0.10) -> float:
    """
    Calcula o valor do imposto sobre uma compra.

    Recebe o valor total e a taxa de imposto.
    Retorna o valor do imposto calculado.
    """
    if not isinstance(valor_total, (int, float)):
        raise TypeError("O valor total deve ser numérico.")
    if not isinstance(taxa, (int, float)):
        raise TypeError("A taxa deve ser numérica.")
    if valor_total < 0 or taxa < 0:
        raise ValueError("Valor total e taxa não podem ser negativos.")
    return round(valor_total * taxa, 2)


def calcular_frete(valor_total: float) -> float:
    """
    Calcula o frete da compra.

    Recebe o valor total da compra.
    Retorna o valor do frete de acordo com a regra definida.
    """
    if not isinstance(valor_total, (int, float)):
        raise TypeError("O valor total deve ser numérico.")
    if valor_total <= 0:
        return 0.0
    if valor_total >= 200:
        return 0.0
    if valor_total >= 100:
        return 7.50
    return 15.00


def validar_cpf_cliente(cpf_texto: str) -> bool:
    """
    Valida um CPF informado pelo cliente.

    Recebe o CPF em texto.
    Retorna True se o CPF for válido e False se não for.
    """
    if not isinstance(cpf_texto, str):
        return False

    cpf = "".join(ch for ch in cpf_texto if ch.isdigit())

    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False

    def calcular_digito(base: str) -> str:
        """
        Calcula um dos dígitos verificadores do CPF.

        Recebe a parte base do CPF.
        Retorna o dígito calculado em formato de texto.
        """
        soma = sum(int(numero) * peso for numero, peso in zip(base, range(len(base) + 1, 1, -1)))
        resto = soma % 11
        return "0" if resto < 2 else str(11 - resto)

    digito1 = calcular_digito(cpf[:9])
    digito2 = calcular_digito(cpf[:9] + digito1)

    return cpf[-2:] == digito1 + digito2


def calcular_total(itens: Iterable[dict]) -> float:
    """
    Calcula o total de vários itens.

    Recebe uma lista ou qualquer conjunto de itens com preço e quantidade.
    Retorna a soma total de todos os produtos.
    """
    total = 0.0

    for item in itens:
        preco = item.get("preco")
        quantidade = item.get("quantidade")

        if not isinstance(preco, (int, float)):
            raise TypeError("Preço inválido.")
        if not isinstance(quantidade, (int, float)):
            raise TypeError("Quantidade inválida.")
        if preco < 0 or quantidade < 0:
            raise ValueError("Preço e quantidade não podem ser negativos.")

        total += float(preco) * float(quantidade)

    return round(total, 2)


def calcular_parcelamento(total: float, parcelas: int) -> float:
    """
    Calcula quanto fica cada parcela.

    Recebe o valor total da compra e a quantidade de parcelas.
    Retorna o valor de cada parcela.
    """
    if not isinstance(total, (int, float)):
        raise TypeError("O total deve ser numérico.")
    if not isinstance(parcelas, int):
        raise TypeError("O número de parcelas deve ser inteiro.")
    if total < 0:
        raise ValueError("O total não pode ser negativo.")
    if parcelas <= 0:
        raise ValueError("A quantidade de parcelas deve ser maior que zero.")
    return round(total / parcelas, 2)


def consultar_produto(produtos: dict, nome: str):
    """
    Busca um produto dentro do dicionário.

    Recebe o dicionário de produtos e o nome do produto.
    Retorna o produto encontrado ou None se não existir.
    """
    if not isinstance(produtos, dict):
        raise TypeError("produtos deve ser um dicionário.")
    if not isinstance(nome, str):
        return None

    nome_normalizado = nome.strip().title()
    return produtos.get(nome_normalizado)