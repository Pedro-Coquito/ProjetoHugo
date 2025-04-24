import os

def verificar_arquivo_existente(arquivo):
    """Verifica se o arquivo já existe. Se existir, pergunta ao usuário se deseja sobrescrever ou abrir o arquivo principal."""
    if os.path.exists(arquivo):
        resposta = input(f"O arquivo '{arquivo}' já existe. Deseja sobrescrevê-lo? (s/n): ")
        if resposta.lower() == 'n':
            print("Abrindo o arquivo principal...")
            # Retorna o nome do arquivo para abrir o arquivo sem sobrescrevê-lo
            return arquivo
        elif resposta.lower() == 's':
            print(f"O arquivo '{arquivo}' será sobrescrito.")
            return arquivo  # Sobrescreve o arquivo
        else:
            print("Resposta inválida. Por favor, digite 's' para sobrescrever ou 'n' para abrir o arquivo.")
            return verificar_arquivo_existente(arquivo)  # Chama novamente para continuar o processo
    else:
        return arquivo  # Retorna o nome do arquivo se não existir

def display_dados(arquivo):
    """Exibe os dados diretamente do arquivo."""
    if arquivo is None:
        print("Erro: Nenhum arquivo válido fornecido!")
        return  # Sai da função se o arquivo for None
    
    try:
        with open(arquivo, "r", encoding="utf-8") as file:
            dados = file.read()  # Lê o conteúdo do arquivo
            if not dados:
                print("o arquivo está vazio.")
            else:
                print("Conteúdo do arquivo:")
                print(dados)  # Exibe o conteúdo do arquivo
    except FileNotFoundError:
        print("Arquivo não encontrado!")
    except IOError:
        print("Erro ao acessar o arquivo.")

def add_number(arquivo):
    """Adiciona um dado diretamente no arquivo."""
    entrada = input("Digite o dado para adicionar ao arquivo:\n")
    try:
        with open(arquivo, "a", encoding="utf-8") as file:  # Abre no modo 'append' para adicionar dados
            file.write(f"{entrada} ")
        print("Dado adicionado com sucesso!")
    except IOError:
        print("Erro ao adicionar dados no arquivo.")

def remove_log(arquivo):
    """Remove o dado informado diretamente no arquivo."""
    try:
        with open(arquivo, "r", encoding="utf-8") as file:
            dados = file.read().split()  # Lê todos os dados do arquivo
            if not dados:
                print("O arquivo está vazio, não há dados para remover.")
                return

        entrada = input("Digite o dado que quer remover:\n")
        
        if entrada in dados:
            dados.remove(entrada)
            # Reescreve o arquivo com os dados restantes
            with open(arquivo, "w", encoding="utf-8") as file:
                for dado in dados:
                    file.write(f"{dado} ")
            print("Dado removido com sucesso!")
        else:
            print("Dado não encontrado no arquivo.")
    except FileNotFoundError:
        print("Arquivo não encontrado!")
    except IOError:
        print("Erro ao modificar o arquivo.")

if __name__ == "__main__":
    arquivo = input("Digite o nome do arquivo: ")
    arquivo = verificar_arquivo_existente(arquivo)

    if arquivo:  # Se o arquivo foi escolhido para ser sobrescrito, prossegue
        while True:
            print("\n===== GERENCIADOR DE DADOS =====")
            print("1. Adicionar dados")
            print("2. Remover dados")
            print("3. Exibir dados")
            print("4. Sair")
            try:
                opcao = int(input("Escolha uma opção: "))
            except ValueError:
                print("Opção inválida! Tente novamente.")
                continue

            if opcao == 1:
                add_number(arquivo)
            elif opcao == 2:
                remove_log(arquivo)
            elif opcao == 3:
                display_dados(arquivo)
            elif opcao == 4:
                print("Saindo do Programa...")
                break
            else:
                print("Opção inválida! Tente novamente.")
    else:
        print("O arquivo foi aberto e o programa continuará com os dados existentes.")
