def verificar_par_ou_impar():
    contagem_pares = 0
    contagem_impares = 0
    
    print("--- Verificador Par ou Ímpar ---")
    print("Insira números inteiros. Digite 'fim' para encerrar e ver o resumo.")

    while True:
        entrada = input("Insira um número inteiro: ")
        
        if entrada.lower() == 'fim':
            break

        try:
            numero = int(entrada)
            
            if numero % 2 == 0:
                contagem_pares += 1
                print(f"-> O número {numero} é PAR.")
            else:
                contagem_impares += 1
                print(f"-> O número {numero} é ÍMPAR.")

        except ValueError:
            print(f"❌ ERRO: '{entrada}' não é um número inteiro válido. Por favor, insira um número inteiro ou 'fim'.")
            continue
    
    print("\n--- Resultado Final ---")
    print(f"Total de números PARES inseridos: {contagem_pares}")
    print(f"Total de números ÍMPARES inseridos: {contagem_impares}")
    print("Programa encerrado.")

if __name__ == "__main__":
    verificar_par_ou_impar()