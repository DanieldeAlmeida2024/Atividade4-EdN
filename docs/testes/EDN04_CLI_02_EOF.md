# EDN04-CLI-02 — Encerramento de entrada em exercícios interativos

14/11/2026 · Registro de notas, senha e paridade.

## Falha encontrada
Três programas mantinham laços de entrada que exigiam o comando `fim`/`sair`. Ao encerrar stdin em terminal, pipe, CI ou PowerShell, a chamada `input()` levantava EOFError e encerrava com traceback.

## Correção
- Notas: EOF finaliza a coleta e calcula média usando somente notas válidas já registradas.
- Paridade: EOF finaliza o laço e mantém contagem de pares/ímpares.
- Verificação de senha: EOF termina sem afirmar que houve senha válida.
- Regressões executam os três scripts como subprocessos com stdin encerrado após dados parciais.

## Escopo
Os critérios de senha permanecem aqueles do exercício educacional, não requisitos de autenticação real.
