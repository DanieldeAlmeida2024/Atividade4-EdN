def verificar_senha_forte(senha):
    if not isinstance(senha, str) or len(senha) < 8:
        return False, "A senha deve ter pelo menos 8 caracteres."

    tem_numero = any(char.isdigit() for char in senha)
    if not tem_numero:
        return False, "A senha deve conter pelo menos um número."

    return True, "Senha atende aos critérios do exercício!"

def validar_senha():
    print("--- Verificador de Senha Forte ---")
    print("Critérios: Mínimo 8 caracteres e pelo menos 1 número.")
    print("Digite 'sair' a qualquer momento para encerrar.")

    while True:
        entrada_senha = input("Insira uma senha: ")
        
        if entrada_senha.strip().lower() == 'sair':
            print("Programa encerrado pelo usuário.")
            break
        
        is_forte, mensagem = verificar_senha_forte(entrada_senha)
        
        if is_forte:
            print(f"\n✅ SUCESSO! {mensagem}")
            break
        else:
            print(f"❌ ERRO: {mensagem} Tente novamente.")

if __name__ == "__main__":
    validar_senha()