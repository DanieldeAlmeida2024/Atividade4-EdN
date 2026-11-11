# Loops, calculadora, notas, senha e paridade

**1.0.0 — 11/11/2026 — código `4fdca05322435b6f0e8f81c5b971607d724f8f58`**. Relato de inspeção, não de execução funcional.

## Visão do projeto
4 programas Python independentes, organizados em arquivos/pastas; são exercícios de linha de comando, não um serviço web. Os scripts fazem leitura/escrita padrão com `input()`/`print()`. Não foi identificada persistência compartilhada.

## Especificação observada
| Fonte | Fluxo / regra efetiva | Critério de aceitação/limite |
|---|---|---|
| `1/calculadora.py` | Input de dois floats (aceita vírgula), operador +,-,*,/ e loop para tentar novamente | 2+3=5; dividir por zero exibe erro sem encerrar |
| `2/registroDeNotas.py` | Insere notas 0..10 até texto fim; calcula média | 0 e 10 geram média 5; turma vazia não divide por zero |
| `3/verificacaoDeSenha.py` | verificar_senha_forte exige 8 caracteres e um dígito | abcdefg1 aceita; abcdefgh e abc1 rejeitados |
| `4/verificadorParOuImpar.py` | Conta inteiros pares/ímpares até fim | -2, 0, 3 = 2 pares, 1 ímpar |

## Decisões, dívida técnica e segurança
O verificador de senha não mede entropia e não é adequado para produção; a calculadora tem loop de recuperação, mas pode exibir exceções não tratadas para valores extremos. Não persistem notas, senhas ou resultados.

Para testes automatizados, isolar funções e substituir `input()` por sequências controladas; não reescrever o comportamento por conveniência. Execute o exercício principal por `python 3/verificacaoDeSenha.py`. A pasta `tests/` atual trata primordialmente estrutura documental. A versão do Python, entrada e stdout precisam ser registradas para confirmar casos.
