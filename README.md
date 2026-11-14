# Atividade4-EdN — exercícios de Python

Exercícios de calculadora com tratamento de erros, notas, senha e verificação de números.

## Requisitos
Python 3.10+ e terminal local. Exercícios separados, não API/serviço em produção.

## Executar um exercício
```bash
python 1/calculadora.py
```

**Outros scripts:** `1/calculadora.py, 2/registroDeNotas.py, 3/verificacaoDeSenha.py, 4/verificadorParOuImpar.py`.

## Testes de comportamento
```bash
python -m unittest discover -s tests -v
```

A suíte executa entradas e saídas dos quatro exercícios, incluindo operações inválidas, recuperação de erros, notas descartadas, senha e contagem par/ímpar.

## Regras e tratamento de erros

- A **calculadora** usa uma função testável, rejeita divisão por zero, operações inválidas, `NaN` e infinito, e permite novas tentativas sem captura genérica de exceções. Ao receber fim de entrada, encerra sem traceback.
- O registro de notas e a contagem par/ímpar reconhecem o comando `fim` mesmo com espaços.
- A validação de senha atende **somente** às regras pedagógicas: mínimo de 8 caracteres e um dígito. Não equivale a uma política de senha segura para sistemas reais.
- O CI executa os testes em Python 3.12, sem dependências externas.

## Navegação
[Requisitos](docs/REQUISITOS.md), [estrutura](docs/ARQUITETURA.md), [UML](docs/UML.puml), [plano de testes](docs/PLANO_TESTES.md) e [guia de IA](AGENTS.md).

---

## Enunciados originais

## Atividade Prática 04

### 1. 
    Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração, multiplicação e divisão) entre dois números. A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as especificações abaixo:



    A calculadora deve solicitar ao usuário que insira dois números e uma operação.

    As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).

    O programa deve continuar solicitando entradas até que uma operação válida seja concluída.

    Trate os seguintes erros:

    Entrada inválida (não numérica) para os números

    Divisão por zero

    Operação inválida



    Use try/except para capturar e tratar os erros apropriadamente.

    Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.

    Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa.




### 2. 
    Crie um programa que permita a um professor registrar as notas de uma turma. O programa deve continuar solicitando notas até que o professor digite 'fim'. Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. No final, deve exibir a média da turma.




### 3. 
    Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.




### 4. 
    Crie um programa que solicite ao usuário que insira números inteiros. O programa deve continuar solicitando números até que o usuário digite 'fim'. Para cada número inserido, o programa deve informar se é par ou ímpar. Se o usuário inserir algo que não seja um número inteiro, o programa deve
    informar o erro e continuar. No final, o programa deve exibir a quantidade de números pares e ímpares inseridos.
