


def main():
    tasks = []
    print("Bem-vindo ao gerenciador de tarefas!")
    while True:
        print("\n1. Adicionar tarefa")
        print("2. Remover tarefa")
        print("3. Listar tarefas")
        print("4. Sair")
        print("5.Limpar tarefas")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            task = input("Digite a tarefa: ")
            tasks.append(task)
            print("Tarefa adicionada!")
        elif choice == "2":
            for idx, t in enumerate(tasks):
                print(f"{idx + 1}. {t}")
            idx = input("Digite o número da tarefa para remover: ")
            if idx.isdigit() and 1 <= int(idx) <= len(tasks):
                removed = tasks.pop(int(idx) - 1)
                print(f"Tarefa '{removed}' removida!")
            else:
                print("Opção inválida.")
        elif choice == "3":
            if tasks:
                print("Tarefas:")
                for idx, t in enumerate(tasks):
                    print(f"{idx + 1}. {t}")
            else:
                print("Nenhuma tarefa.")
        elif choice == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
    
if __name__ == "__main__":
    
    main()