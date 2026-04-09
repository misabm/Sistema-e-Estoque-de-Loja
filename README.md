# Sistema de Estoque e Loja

Este é um sistema de linha de comando (CLI) desenvolvido em Python para gerenciar o estoque e as operações de venda de uma loja. O projeto foi construído de forma modularizada, separando as lógicas de negócio, operações matemáticas, interface com o usuário e testes automatizados.

## 📌 Funcionalidades

**Gerenciamento de Estoque:**
- Cadastro, edição e remoção de produtos.
- Listagem de produtos e consulta de valor total em estoque.
- Alerta automático de produtos com estoque baixo.

**Operações de Loja (Frente de Caixa):**
- Registro de compras com atualização automática (baixa) no estoque.
- Consulta de produtos disponíveis para venda.
- Validação de CPF para inclusão na nota.
- Cálculos financeiros integrados:
  - Aplicação de descontos.
  - Cálculo de impostos.
  - Cálculo de frete (Frete grátis para compras acima de R$ 200,00).
  - Simulação de parcelamento.
  - Cálculo de troco.

## 📁 Estrutura do Projeto

- `main.py`: Ponto de entrada da aplicação. Inicializa o menu principal.
- `loja/menu.py`: Gerencia a navegação entre os sistemas de Loja e Estoque.
- `loja/estoque.py`: Contém a lógica de armazenamento e gestão dos produtos.
- `loja/loja.py`: Lida com as interações de venda, carrinho de compras e pagamentos.
- `loja/operacoes.py`: Módulo utilitário com regras de negócio, cálculos matemáticos e validação de CPF.
- `tests/test_operacoes.py`: Testes unitários para garantir a integridade das funções matemáticas e de validação.

## 🚀 Como executar o projeto

**Pré-requisitos:**
- Python 3.x instalado na máquina.

**Passo a passo:**
1. Clone este repositório para a sua máquina local:
   ```bash
   git clone [https://github.com/misabm/Sistema-e-Estoque-de-Loja.git]
