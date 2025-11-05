def registrar_notas():
    notas = []
    
    print("--- Registro de Notas da Turma ---")
    print("Insira as notas (entre 0 e 10). Digite 'fim' para calcular a média e sair.")

    while True:
        entrada = input("Nota: ")
        
        if entrada.lower() == 'fim':
            break

        try:
            nota = float(entrada.replace(',', '.'))
            
            if 0 <= nota <= 10:
                notas.append(nota)
                print(f"✅ Nota {nota} registrada. Total de notas: {len(notas)}")
            else:
                print("⚠️ NOTA INVÁLIDA: A nota deve estar entre 0 e 10. Tente novamente.")
                continue 

        except ValueError:
            print(f"⚠️ ENTRADA INVÁLIDA: '{entrada}' não é um número nem o comando 'fim'. Tente novamente.")
            continue

    print("\n--- Resultados Finais ---")
    
    if notas:
        total_notas = len(notas)
        soma_notas = sum(notas)
        media = soma_notas / total_notas
        
        print(f"Número de notas válidas registradas: {total_notas}")
        print(f"Soma total das notas: {soma_notas:.2f}")
        print(f"Média da turma: **{media:.2f}**")
    else:
        print("Nenhuma nota válida foi registrada.")

if __name__ == "__main__":
    registrar_notas()