def calcular_parcelamento(total: float, parcelas: int) -> float:
    if parcelas <= 0:
        raise ValueError("A quantidade de parcelas deve ser maior que zero.")
    if total < 0:
        raise ValueError("O total não pode ser negativo.")
    if not isinstance(parcelas, int):
        raise TypeError("O número de parcelas deve ser um inteiro.")

    valor_parcela = total / parcelas
    return round(valor_parcela, 2)   