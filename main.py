"""
Simulador de Saque em Caixa Eletrônico

Este programa simula o funcionamento de um caixa eletrônico que realiza a distribuição de cédulas para um saque
solicitado pelo usuário.

O sistema calcula a menor quantidade possível de cédulas necessárias para entregar o valor solicitado, utilizando as
seguintes denominações:

- R$100
- R$50
- R$20
- R$10
- R$5
- R$2

Funcionalidades:
- Receber o valor do saque
- Validar se a entrada é numérica
- Garantir que o valor seja múltiplo de 2
- Calcular a quantidade mínima de cédulas necessárias
- Exibir as cédulas que serão entregues

Conceitos praticados:
- Divisão inteira (//)
- Resto da divisão (%)
- Estruturas de repetição
- Dicionários
- Tratamento de exceções
- Organização de código com funções
"""
TITULO = "Simulador de Saque em Caixa Eletrônico"
TAMANHO_LINHA = 78
CEDULAS = [100, 50, 20, 10, 5, 2]


def calcular_cedulas(valor: int) -> dict:
    """
    Calcula a quantidade mínima de cédulas necessárias para um saque.

    Parâmetros:
        valor (int): Valor total solicitado para o saque.

    Retorna:
        dict: Um dicionário onde as chaves representam o valor das cédulas
        e os valores representam a quantidade de cada cédula utilizada

    """
    resultado = {}

    for cedula in CEDULAS:
        quantidade = valor // cedula
        valor = valor % cedula

        if quantidade > 0:
            resultado[cedula] = quantidade

    return resultado


def exibir_cedulas(resultado: dict):
    """
    Exibe no terminal as cédulas que serão entregues no saque.

    Parâmetros:
    resultado (dict): Dicionário contendo o valor das cédulas como chave
    e a quantidade de cada uma como valor.
    """
    print("Cédulas entregues:")

    for cedula, quantidade in resultado.items():
        print(f"{quantidade} de R$ {cedula}")


def main():
    """Controla o fluxo principal do programa."""
    print(TAMANHO_LINHA * "=")
    print(TITULO.center(TAMANHO_LINHA))
    print(TAMANHO_LINHA * "=")

    try:
        valor = int(input("Insira o valor do saque: "))
    except ValueError:
        print("Erro: Entrada inválida. Digite um valor numérico.")
        return

    if valor % 2 != 0:
        print("Erro: O valor deve ser múltiplo de 2.")
        return

    print(TAMANHO_LINHA * "=")
    resultado = calcular_cedulas(valor)
    exibir_cedulas(resultado)
    print(TAMANHO_LINHA * "=")


if __name__ == "__main__":
    main()
