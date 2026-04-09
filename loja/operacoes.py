from typing import Iterable


def aplicar_desconto(total: float, porcentagem: float) -> float:
    """Aplica desconto percentual sobre um total e retorna o valor final."""
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
    """Calcula o troco de uma compra e levanta erro se o valor pago for insuficiente."""
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
    """Calcula o imposto sobre um valor total."""
    if not isinstance(valor_total, (int, float)):
        raise TypeError("O valor total deve ser numérico.")
    if not isinstance(taxa, (int, float)):
        raise TypeError("A taxa deve ser numérica.")
    if valor_total < 0 or taxa < 0:
        raise ValueError("Valor total e taxa não podem ser negativos.")
    return round(valor_total * taxa, 2)


def calcular_frete(valor_total: float) -> float:
    """Calcula o frete com base no valor total da compra."""
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
    """Valida um CPF usando a regra dos dígitos verificadores."""
    if not isinstance(cpf_texto, str):
        return False

    cpf = "".join(ch for ch in cpf_texto if ch.isdigit())

    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False

    def calcular_digito(base: str) -> str:
        soma = sum(int(numero) * peso for numero, peso in zip(base, range(len(base) + 1, 1, -1)))
        resto = soma % 11
        return "0" if resto < 2 else str(11 - resto)

    digito1 = calcular_digito(cpf[:9])
    digito2 = calcular_digito(cpf[:9] + digito1)

    return cpf[-2:] == digito1 + digito2


def calcular_total(itens: Iterable[dict]) -> float:
    """Calcula o total de uma lista de itens com preço e quantidade."""
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
    """Calcula o valor de cada parcela."""
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
    """Consulta um produto no dicionário de produtos pelo nome normalizado."""
    if not isinstance(produtos, dict):
        raise TypeError("produtos deve ser um dicionário.")
    if not isinstance(nome, str):
        return None

    nome_normalizado = nome.strip().title()
    return produtos.get(nome_normalizado)