"""Calculadora interativa com recuperação de erros de entrada."""
import math

OPERACOES = ('+', '-', '*', '/')

def calcular(numero1: float, numero2: float, operacao: str) -> float:
    if not all(isinstance(x, (float, int)) and math.isfinite(x) for x in (numero1, numero2)):
        raise ValueError("Informe números reais finitos.")
    if operacao not in OPERACOES:
        raise ValueError("Operação inválida. Use +, -, * ou /.")
    if operacao == '/' and numero2 == 0:
        raise ValueError("Não é possível dividir por zero.")
    if operacao == '+':
        resultado = numero1 + numero2
    elif operacao == '-':
        resultado = numero1 - numero2
    elif operacao == '*':
        resultado = numero1 * numero2
    else:
        resultado = numero1 / numero2
    if not math.isfinite(resultado):
        raise ValueError("O resultado excede o limite numérico suportado.")
    return resultado

def calculadora():
    while True:
        print("\n--- Calculadora Simples ---")
        try:
            numero1 = float(input("Insira o primeiro número: ").replace(',', '.'))
            numero2 = float(input("Insira o segundo número: ").replace(',', '.'))
            operacao = input("Insira a operação (+, -, *, /): ").strip()
            resultado = calcular(numero1, numero2, operacao)
        except EOFError:
            print("Entrada encerrada.")
            return
        except ValueError as erro:
            print(f"ERRO: {erro} Tente novamente.")
            continue

        print("\nOperação bem-sucedida:")
        print(f"O resultado de {numero1} {operacao} {numero2} é: {resultado}")
        return

if __name__ == "__main__":
    calculadora()
