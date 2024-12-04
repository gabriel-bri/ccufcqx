from funcoes import *

def exibir_menu():
    print("\n--- MENU ---")
    print("1. Gerar chaves de criptografia.")
    print("2. Criptografar arquivo. (apenas .txt)")
    print("3. Descriptografar arquivo. (apenas .txt)")
    print("4. Comparar hashes.")
    print("5. Criar novo arquivo de teste. (apenas .txt)")
    print("6. Criar novo arquivo vazio. (apenas .txt)")
    print("7. Apagar conteúdo do arquivo. (apenas .txt)")
    print("8. Inserir conteúdo no arquivo. (apenas .txt)")
    print("9. Ler conteúdo do arquivo")
    print("10. Apagar arquivo.")
    print("11. Listar arquivos no diretório.")
    print("12. Limpar a tela.")
    print("13. Rever o menu.")
    print("0. Sair")

def menu():
    exibir_menu()
    while True:
        opcao = input("Escolha uma opção: ")        
        if opcao == "1":
            if not gerar_chaves():
                continue
        if opcao == "2":
            if not validar_criptografia():
                continue
        if opcao == "3":
            if not validar_descriptografia():
                continue         
        if opcao == "4":
            if not validar_hash():
                continue         
        elif opcao == "5":
            if not criar_arquivo():
                continue
        elif opcao == "6":
            if not criar_arquivo_vazio():
                continue
        elif opcao == "7":
            apagar_conteudo()
        elif opcao == "8":
            inserir_conteudo()
        elif opcao == "9":
            ler_conteudo()
        elif opcao == "10":
            apagar_arquivo()
        elif opcao == "11":
            listar_arquivos()
        elif opcao == "12":
            limpar_tela()
        elif opcao == "13":
            exibir_menu()
        elif opcao == "0":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")
