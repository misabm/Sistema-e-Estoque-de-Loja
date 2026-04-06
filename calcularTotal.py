from typing import Iterable

def calcular_total(itens: Iterable[dict]) -> float:

    total = 0.0
    for item in itens:
        preco = item.get("preco", 0)
        quantidade = item.get("quantidade", 0)
        
        if not isinstance(preco, (int, float)):
            raise TypeError(f"Preço inválido: {preco} (deve ser número)")
        if not isinstance(quantidade, (int, float)):
            raise TypeError(f"Quantidade inválida: {quantidade} (deve ser número)")
        
        total += preco * quantidade
    
    return round(total, 2)   # arredondamento essencial