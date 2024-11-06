tasks = []  # Список задач


def add_task():
    # Ввод данных от пользователя
    task_name = input("Введите название задачи: ")
    priority = int(
        input("Введите приоритет задачи (1 - высокий, 2 - средний, 3 - низкий): "))
    is_completed = input("Задача выполнена? (да/нет): ").lower() == "да"

    # Добавляем задачу в список
    tasks.append({"name": task_name, "priority": priority,
                 "completed": is_completed})


def display_tasks():
    # Сортировка задач по приоритету
    tasks.sort(key=lambda x: x["priority"])

    print("\n--- Список задач ---")
    for task in tasks:
        status = "Выполнено" if task["completed"] else "Не выполнено"
        print(f"Задача: {task['name']}, Приоритет: {task['priority']}, Статус: {status}")


def main():
    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Показать все задачи")
        print("3. Выход")

        choice = input("Выберите опцию: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
