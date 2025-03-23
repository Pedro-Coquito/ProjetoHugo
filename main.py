import os

def load_dados(arquivo):
    """Carrega os números do arquivo para uma lista."""
    dados = []
    try:
        with open(arquivo, "r", encoding="utf-8") as file:
            # Lê todos os números presentes no arquivo
            for token in file.read().split():
                try:
                    dados.append(int(token))
                except ValueError:
                    continue
    except FileNotFoundError:
        print("Não foi possível carregar o arquivo!", arquivo)
    return dados

def save_dados(dados, arquivo):
    """Salva os números da lista no arquivo."""
    try:
        with open(arquivo, "w", encoding="utf-8") as file:
            for num in dados:
                file.write(f"{num} ")
            file.write("\n")
    except IOError:
        print("Erro: Nenhum arquivo encontrado!", dados)

def display_dados(dados):
    """Exibe os números com sua posição."""
    if not dados:
        print("A lista está vazia")
    else:
        print("Lista de números")
        for idx, num in enumerate(dados, start=1):
            print(f"{idx}. {num}")

def add_number(dados, arquivo):
    """Adiciona um número à lista e salva no arquivo."""
    try:
        num = int(input("Digite um número para adicionar a lista:\n"))
        dados.append(num)
        save_dados(dados, arquivo)
        print("Número adicionado com sucesso!!")
    except ValueError:
        print("Entrada inválida!")

def remove_number(dados, arquivo):
    """Remove o número informado da lista, se existir, e salva no arquivo."""
    if not dados:
        print("A lista está vazia, não há números para serem removidos.")
        return
    try:
        num = int(input("Digite o número que deseja remover!\n"))
        if num in dados:
            dados.remove(num)
            save_dados(dados, arquivo)
            print("Número removido com sucesso!!")
        else:
            print("Número não encontrado na lista!!")
    except ValueError:
        print("Entrada inválida!")

def sort_dados(dados, arquivo):
    """Ordena os números em ordem crescente, se necessário, e salva no arquivo."""
    if not dados:
        print("A lista está vazia, nenhum número para ordenar!!")
        return
    if dados == sorted(dados):
        print("A lista já está ordenada!!")
    else:
        dados.sort()
        print("Lista ordenada em ordem crescente")
        save_dados(dados, arquivo)

def find_number(dados, arquivo):
    """Busca um número na lista e exibe as posições em que ele aparece."""
    if not dados:
        print("A lista está vazia, nenhum número para encontrar!")
        return
    try:
        num = int(input("Digite o número que quer encontrar:\n"))
        indices = [i + 1 for i, n in enumerate(dados) if n == num]
        if indices:
            print("Número encontrado nas posições:", " ".join(str(pos) for pos in indices))
        else:
            print("Número não encontrado na lista!!")
        save_dados(dados, arquivo)
    except ValueError:
        print("Entrada inválida!")

def main():
    # Limpa a tela: 'cls' para Windows, 'clear' para sistemas Unix
    os.system("cls" if os.name == "nt" else "clear")
    arquivo = "Lista Numeros.txt"
    dados = load_dados(arquivo)

    while True:
        print("\n===== GERENCIADOR DE NÚMEROS =====")
        print("1. Adicionar número")
        print("2. Remover número")
        print("3. Exibir números")
        print("4. Ordenar números")
        print("5. Buscar número")
        print("6. Sair")
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida! Tente novamente.")
            continue

        if opcao == 1:
            add_number(dados, arquivo)
        elif opcao == 2:
            remove_number(dados, arquivo)
        elif opcao == 3:
            display_dados(dados)
        elif opcao == 4:
            sort_dados(dados, arquivo)
        elif opcao == 5:
            find_number(dados, arquivo)
        elif opcao == 6:
            print("Saindo do Programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
