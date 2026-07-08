from analisadorLexico import construir_dfa, analisador_lexico
import os

def main():
    print("Construindo DFA...")
    estado_inicial, transicoes, finais_dict = construir_dfa()
    print(f"DFA pronto com {len(transicoes)} estados!\n")
    print("DFA pronto!\n")

    while True:
        print("Como deseja fornecer o codigo?")
        print("1 - Carregar arquivo")
        print("2 - Digitar manualmente")
        print("3 - Sair")
        opcao = input("\nEscolha (1, 2 ou 3): ").strip()

        if opcao == "1":
            nome_arquivo = "testes_lexico.txt"
            if not os.path.exists(nome_arquivo):
                print(f"Arquivo '{nome_arquivo}' não encontrado.\n")
                continue
            with open(nome_arquivo, 'r', encoding='utf-8') as f:
                codigo = f.read()
            saidas = analisador_lexico(codigo, estado_inicial, transicoes, finais_dict)
            print("\n--- Resultado ---")
            for saida in saidas:
                print(saida)
            print("-----------------\n")

        elif opcao == "2":
            print("\nModo manual. Digite 'sair' para voltar ao menu.\n")
            while True:
                linha = input("> ")
                if linha.lower() == 'sair':
                    break
                if linha.strip() == "":
                    continue
                saidas = analisador_lexico(linha, estado_inicial, transicoes, finais_dict)
                for saida in saidas:
                    print(saida)

        elif opcao == "3":
            print("Encerrando...")
            return

        else:
            print("Opção inválida.\n")

if __name__ == "__main__":
    main()