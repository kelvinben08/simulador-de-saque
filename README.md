# Simulador de Saque em Caixa Eletrônico
- Este projeto é um simulador simples de saque em um caixa eletrônico desenvolvido em Python.
- O programa recebe um valor de saque informado pelo usuário e calcula a menor quantidade de cédulas necessária para entregar o valor solicitado.

---

### Cédulas disponíveis
- O sistema trabalha com as seguintes cédulas:
  - R$100
  - R$50
  - R$20
  - R$10
  - R$5
  - R$2

---

### Exemplo de uso
- Entrada:
```
Digite o valor do saque: 188
```
- Saída:
```
Cédulas entregues:
1 de R$ 100
1 de R$ 50
1 de R$ 20
1 de R$ 10
1 de R$ 5
1 de R$ 2
```

---

### Funcionalidades
- Receber valor de saque
- Validar entrada do usuário
- Garantir que o valor seja múltiplo de 2
- Calcular a menor quantidade de cédulas
- Exibir as cédulas que serão entregues

---

### Conceitos praticados
- Este projeto foi desenvolvido para praticar conceitos fundamentais de programação em Python:
  - divisão inteira (`//`)
  - resto da divisão (`%`)
  - estruturas de repetição (`for`)
  - dicionários
  - tratamento de exceções (`try / except`)
  - organização de código com funções
  - separação de responsabilidades
  - função `main()`

---

### Estrutura do projeto
- main.py
- O arquivo contém:
  - cálculo da distribuição de cédulas
  - exibição do resultado
  - controle do fluxo principal do programa

---

## Como executar
1. Clone o repositório:
```
git clone <url-do-repositorio>
```

2. Execute o programa:
```
python main.py
```

3. Informe o valor do saque quando solicitado.
