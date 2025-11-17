print('==== Boas-Vindas à sua agenda digital! ====')

days = {
    "segunda": [],
    "terça": [],
    "quarta": [],
    "quinta": [],
    "sexta": [],
    "sábado": [],
    "domingo": []
}

# Função para mostrar o menu
def menu():
    print("\nMenu de opções:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Remover tarefa")
    print("0. Sair")
    choice = input("Escolha uma opção: ")
    return choice

# Função para adicionar tarefa
def add_task():
    while True:
        print("\nEscolha um dia da semana para adicionar uma tarefa: ")
        print("1. Segunda")
        print("2. Terça")
        print("3. Quarta")
        print("4. Quinta")
        print("5. Sexta")
        print("6. Sábado")
        print("7. Domingo")
        print("0. Sair")

        day_choice = input("Digite sua escolha: ")

        if day_choice == "0":
            break

        day_map = {
            "1": "segunda",
            "2": "terça",
            "3": "quarta",
            "4": "quinta",
            "5": "sexta",
            "6": "sábado",
            "7": "domingo"
        }

        day = day_map.get(day_choice)

        if day:
            title = input("Adicione um título curto para a tarefa: ")
            task = input("Descreva de forma sucinta a tarefa que deseja adicionar (max. 10 palavras): ")
            days[day].append({"titulo": title, "tarefa": task})
            print(f"Tarefa adicionada com sucesso no(a) {day}!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Função para visualizar as tarefas
def view_tasks():
    print("\nTarefas da semana: ")
    for day, tasks in days.items():
        print(f"\n{day.capitalize()}:")
        if tasks:
            for task in tasks:
                print(f"- {task["titulo"]}: {task["tarefa"]}")
        else:
            print("Nenhuma tarefa para este dia.")
    print()

# Função para remover tarefa
def remove_task():
    day_choice = input("\nEscolha um dia da semana para remover uma tarefa (segunda, terça...): ").lower()
    if day_choice in days:
        if days[day_choice]:
            print(f"\nTarefas em {day_choice.capitalize()}:")
            for i, task in enumerate(days[day_choice]):
                print(f"{i +1}. {task["titulo"]} - {task["tarefa"]}")
                task_index = int(input("Digite o número da tarefa que deve ser excluída:")) -1
                if 0<= task_index < len (days[day_choice]):
                    removed_task = days[day_choice].pop(task_index)
                    print(f"Tarefa '{removed_task["titulo"]} ' removida com sucesso!")
                else:
                    print("Número inválido. Tente novamente.")
            else:
                print(f"Nenhuma tarefa para {day_choice}.")
    else:
        print("Dia inválido. Tente novamente.")

# Loop principal
while True:
    choice = menu()
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()   
    elif choice == "3":
        remove_task()
    elif choice == "0":
        break
    else:
        print("Opção inválida. Tente novamente.")         
