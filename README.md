# Atividade4-EdN — exercícios de Python

Exercícios de calculadora com tratamento de erros, notas, senha e verificação de números.

## Requisitos
Python 3.10+ e terminal local. Exercícios separados, não API/serviço em produção.

## Executar um exercício
```bash
python 1/calculadora.py
```

**Outros scripts:** `1/calculadora.py, 2/registroDeNotas.py, 3/verificacaoDeSenha.py, 4/verificadorParOuImpar.py`.

## Verificar sintaxe e documentação
```bash
python -m unittest discover -s tests -v
```

O teste acima **não** compara respostas dos exercícios aos enunciados; esses cenários precisam de testes de comportamento adicionais.

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
