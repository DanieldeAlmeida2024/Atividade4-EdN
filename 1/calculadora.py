def calculadora():
    operacoes_validas = ['+', '-', '*', '/']

    while True:
        print("\n--- Calculadora Simples ---")
        
        try:
            num1_str = input("Insira o primeiro número: ").replace(',', '.')
            numero1 = float(num1_str)
        except ValueError:
            print("❌ ERRO: Entrada inválida. O primeiro valor deve ser um número.")
            continue

        try:
            num2_str = input("Insira o segundo número: ").replace(',', '.')
            numero2 = float(num2_str)
        except ValueError:
            print("❌ ERRO: Entrada inválida. O segundo valor deve ser um número.")
            continue

        operacao = input("Insira a operação (+, -, *, /): ")
        
        if operacao not in operacoes_validas:
            print(f"❌ ERRO: Operação inválida. As operações permitidas são: {', '.join(operacoes_validas)}")
            continue

        try:
            resultado = None
            if operacao == '+':
                resultado = numero1 + numero2
            elif operacao == '-':
                resultado = numero1 - numero2
            elif operacao == '*':
                resultado = numero1 * numero2
            elif operacao == '/':
                resultado = numero1 / numero2
            
            print(f"\n✅ Operação bem-sucedida:")
            print(f"O resultado de {numero1} {operacao} {numero2} é: **{resultado}**")
            break

        except ZeroDivisionError:
            print("❌ ERRO: Não é possível dividir por zero.")
            continue
        except Exception as e:
            print(f"❌ ERRO Inesperado: {e}")
            continue


if __name__ == "__main__":
    calculadora()