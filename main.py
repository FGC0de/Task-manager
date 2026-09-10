tarefas = []


def adicionar_tarefa():
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append({"nome": tarefa, "concluida": False})
    print("Tarefa adicionada!")


def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\n--- Tarefas ---")

    for i, tarefa in enumerate(tarefas, start=1):
        status = "X" if tarefa["concluida"] else " "
        print(f"{i}. [{status}] {tarefa['nome']}")

def concluir_tarefa():
    listar_tarefas()

    if not tarefas:
        return

    try:
        numero = int(input("Digite o número da tarefa: "))

        if 1 <= numero <= len(tarefas):
            tarefas[numero - 1]["concluida"] = True
            print("Tarefa concluída!")
        else:
            print("Número inválido.")

    except ValueError:
        print("Digite um número válido.")


def remover_tarefa():
    listar_tarefas()

    if not tarefas:
        return

    try:
        numero = int(input("Digite o número da tarefa: "))

        if 1 <= numero <= len(tarefas):
            tarefas.pop(numero - 1)
            print("Tarefa removida!")
        else:
            print("Número inválido.")

    except ValueError:
        print("Digite um número válido.")

def buscar_tarefa():
    termo = input("Digite o termo para buscar: ").lower()

    resultados = [
        tarefa for tarefa in tarefas
        if termo in tarefa["nome"].lower()
    ]

    if not resultados:
        print("Nenhuma tarefa encontrada.")
        return

    print("\n--- Resultados ---")

    for i, tarefa in enumerate(resultados, start=1):
        status = "X" if tarefa["concluida"] else " "
        print(f"{i}. [{status}] {tarefa['nome']}")

def menu():
    while True:
        print("\n=== TASK MANAGER ===")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Concluir tarefa")
        print("4. Remover tarefa")
        print("5. Buscar tarefa")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            remover_tarefa()
        elif opcao == "5":
            buscar_tarefa()
        elif opcao == "6":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()

