# Testes específicos de Atividade4-EdN

**1.0.0 — 11/11/2026 — código `4fdca05322435b6f0e8f81c5b971607d724f8f58`**. Relato de inspeção, não de execução funcional.

## Matriz por exercício
| Caso | Arquivo | Entrada e resultado esperado | Evidência |
|---|---|---|---|
| EDT-01 | `1/calculadora.py` | 2+3=5; dividir por zero exibe erro sem encerrar | A executar |
| EDT-02 | `2/registroDeNotas.py` | 0 e 10 geram média 5; turma vazia não divide por zero | A executar |
| EDT-03 | `3/verificacaoDeSenha.py` | abcdefg1 aceita; abcdefgh e abc1 rejeitados | A executar |
| EDT-04 | `4/verificadorParOuImpar.py` | -2, 0, 3 = 2 pares, 1 ímpar | A executar |

## Negativos e não regressão
NT-01: texto não numérico nas leituras. NT-02: números negativos, zero e limites citados nos scripts. NT-03: saída em português e controle de laço/encerramento. NT-04: avaliar `EOFError` e `KeyboardInterrupt` quando o processo for automatizado.

## Execução
```bash
python 3/verificacaoDeSenha.py
python -m unittest discover -s tests -v
```

Casos EDT-* são planejados e não estão cobertos integralmente pelos testes documentais. O registro de cada teste deve conter SHA, stdin, stdout, código de saída, PASS/FAIL/BLOCKED e decisão sobre bugs conhecidos.
