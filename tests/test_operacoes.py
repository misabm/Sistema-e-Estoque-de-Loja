import unittest

from loja.operacoes import (
    aplicar_desconto,
    calcular_frete,
    calcular_imposto,
    calcular_parcelamento,
    calcular_total,
    calcular_troco,
    consultar_produto,
    validar_cpf_cliente,
)


class TestAplicarDesconto(unittest.TestCase):
    def test_desconto_valido(self):
        self.assertEqual(aplicar_desconto(100, 10), 90.0)

    def test_desconto_invalido(self):
        with self.assertRaises(ValueError):
            aplicar_desconto(100, 120)


class TestCalcularTroco(unittest.TestCase):
    def test_troco_valido(self):
        self.assertEqual(calcular_troco(50, 30), 20.0)

    def test_troco_insuficiente(self):
        with self.assertRaises(ValueError):
            calcular_troco(20, 30)


class TestCalcularImposto(unittest.TestCase):
    def test_imposto_valido(self):
        self.assertEqual(calcular_imposto(100), 10.0)

    def test_imposto_invalido(self):
        with self.assertRaises(ValueError):
            calcular_imposto(-10)


class TestCalcularFrete(unittest.TestCase):
    def test_frete_gratuito(self):
        self.assertEqual(calcular_frete(250), 0.0)

    def test_frete_medio(self):
        self.assertEqual(calcular_frete(150), 7.5)


class TestValidarCpfCliente(unittest.TestCase):
    def test_cpf_valido(self):
        self.assertTrue(validar_cpf_cliente("529.982.247-25"))

    def test_cpf_invalido(self):
        self.assertFalse(validar_cpf_cliente("111.111.111-11"))


class TestCalcularTotal(unittest.TestCase):
    def test_total_valido(self):
        itens = [
            {"preco": 10, "quantidade": 2},
            {"preco": 5.5, "quantidade": 1},
        ]
        self.assertEqual(calcular_total(itens), 25.5)

    def test_total_invalido(self):
        itens = [{"preco": "dez", "quantidade": 2}]
        with self.assertRaises(TypeError):
            calcular_total(itens)


class TestCalcularParcelamento(unittest.TestCase):
    def test_parcelamento_valido(self):
        self.assertEqual(calcular_parcelamento(100, 4), 25.0)

    def test_parcelamento_invalido(self):
        with self.assertRaises(ValueError):
            calcular_parcelamento(100, 0)


class TestConsultarProduto(unittest.TestCase):
    def test_consulta_valida(self):
        produtos = {
            "Mouse": {"preco": 50, "quantidade": 3}
        }
        resultado = consultar_produto(produtos, "mouse")
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado["preco"], 50)

    def test_consulta_invalida(self):
        produtos = {
            "Mouse": {"preco": 50, "quantidade": 3}
        }
        self.assertIsNone(consultar_produto(produtos, "teclado"))


if __name__ == "__main__":
    unittest.main()