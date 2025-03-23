import os

def load_numbers(filename):
    """Carrega os números do arquivo para uma lista."""
    numbers = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            # Lê todos os números presentes no arquivo
            for token in file.read().split():
                try:
                    numbers.append(int(token))
                except ValueError:
                    continue
    except FileNotFoundError:
        print("Não foi possível carregar o arquivo!", filename)
    return numbers

def save_numbers(numbers, filename):
    """Salva os números da lista no arquivo."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for num in numbers:
                file.write(f"{num} ")
            file.write("\n")
    except IOError:
        print("Erro: Nenhum arquivo encontrado!", filename)

def display_numbers(numbers):
    """Exibe os números com sua posição."""
    if not numbers:
        print("A lista está vazia")
    else:
        print("Lista de números")
        for idx, num in enumerate(numbers, start=1):
            print(f"{idx}. {num}")

def add_number(numbers, filename):
    """Adiciona um número à lista e salva no arquivo."""
    try:
        num = int(input("Digite um número para adicionar a lista:\n"))
        numbers.append(num)
        save_numbers(numbers, filename)
        print("Número adicionado com sucesso!!")
    except ValueError:
        print("Entrada inválida!")

def remove_number(numbers, filename):
    """Remove o número informado da lista, se existir, e salva no arquivo."""
    if not numbers:
        print("A lista está vazia, não há números para serem removidos.")
        return
    try:
        num = int(input("Digite o número que deseja remover!\n"))
        if num in numbers:
            numbers.remove(num)
            save_numbers(numbers, filename)
            print("Número removido com sucesso!!")
        else:
            print("Número não encontrado na lista!!")
    except ValueError:
        print("Entrada inválida!")

def sort_numbers(numbers, filename):
    """Ordena os números em ordem crescente, se necessário, e salva no arquivo."""
    if not numbers:
        print("A lista está vazia, nenhum número para ordenar!!")
        return
    if numbers == sorted(numbers):
        print("A lista já está ordenada!!")
    else:
        numbers.sort()
        print("Lista ordenada em ordem crescente")
        save_numbers(numbers, filename)

def find_number(numbers, filename):
    """Busca um número na lista e exibe as posições em que ele aparece."""
    if not numbers:
        print("A lista está vazia, nenhum número para encontrar!")
        return
    try:
        num = int(input("Digite o número que quer encontrar:\n"))
        indices = [i + 1 for i, n in enumerate(numbers) if n == num]
        if indices:
            print("Número encontrado nas posições:", " ".join(str(pos) for pos in indices))
        else:
            print("Número não encontrado na lista!!")
        save_numbers(numbers, filename)
    except ValueError:
        print("Entrada inválida!")

def main():
    # Limpa a tela: 'cls' para Windows, 'clear' para sistemas Unix
    os.system("cls" if os.name == "nt" else "clear")
    filename = "Lista Numeros.txt"
    numbers = load_numbers(filename)

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
            add_number(numbers, filename)
        elif opcao == 2:
            remove_number(numbers, filename)
        elif opcao == 3:
            display_numbers(numbers)
        elif opcao == 4:
            sort_numbers(numbers, filename)
        elif opcao == 5:
            find_number(numbers, filename)
        elif opcao == 6:
            print("Saindo do Programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
