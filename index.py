print('==== Boas-Vindas à sua agenda digital! ====')

#Dicionário que armazena os dias da semana com listas vazias.
dias = {
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
    escolha = input("Escolha uma opção: ")
    return escolha

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
        print("0. Sair") # Loop while true que mostra ao usuário um menu com as opções disponíveis.

        dia = input("Digite sua escolha: ")

        if dia == "0":
            break

        dias_map = {
            "1": "segunda",
            "2": "terça",
            "3": "quarta",
            "4": "quinta",
            "5": "sexta",
            "6": "sábado",
            "7": "domingo"
        }

        day = dias_map.get(dia)

        # Aqui, se o dia for válido a tarefa é adicionada ao dicionário "dias" no dia correspondente.
        if day:
            title = input("Adicione um título curto para a tarefa: ")
            task = input("Descreva de forma sucinta a tarefa que deseja adicionar (max. 10 palavras): ")
            dias[dia].append({"titulo": title, "tarefa": task})
            print(f"Tarefa adicionada com sucesso no(a) {day}!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Função para visualizar as tarefas
def view_tasks():
    print("\nTarefas da semana: ")
    for day, tasks in dias.items(): # O for in itera sobre cada item do dicionário "dias".
        print(f"\n{day.capitalize()}:")
        if tasks:
            for task in tasks:
                print(f"- {task["titulo"]}: {task["tarefa"]}")
        else:
            print("Nenhuma tarefa para este dia.")
    print()

# Função para remover tarefa
def remove_task():
    day_escolha = input("\nEscolha um dia da semana para remover uma tarefa (segunda, terça...): ").lower()
    if day_escolha in days:
        if days[day_escolha]:
            print(f"\nTarefas em {day_escolha.capitalize()}:")
            for i, task in enumerate(days[day_escolha]):
                print(f"{i +1}. {task["titulo"]} - {task["tarefa"]}")
                task_index = int(input("Digite o número da tarefa que deve ser excluída:")) -1
                if 0<= task_index < len (days[day_escolha]):
                    removed_task = days[day_escolha].pop(task_index)
                    print(f"Tarefa '{removed_task["titulo"]} ' removida com sucesso!")
                else:
                    print("Número inválido. Tente novamente.")
            else:
                print(f"Nenhuma tarefa para {day_escolha}.")
    else:
        print("Dia inválido. Tente novamente.")

# Loop principal
while True:
    escolha = menu()
    if escolha == "1":
        add_task()
    elif escolha == "2":
        view_tasks()   
    elif escolha == "3":
        remove_task()
    elif escolha == "0":
        break
    else:
        print("Opção inválida. Tente novamente.")         
