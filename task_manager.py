class Task:
    def __init__(self, name, priority, completed=False):
        self.name = name
        self.priority = priority
        self.completed = completed

    def display(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        print(f"Задача: {self.name}, Приоритет: {self.priority}, Статус: {status}")


tasks = []  # Список задач


def add_task():
    # Ввод данных от пользователя
    task_name = input("Введите название задачи: ")
    priority = int(
        input("Введите приоритет задачи (1 - высокий, 2 - средний, 3 - низкий): "))
    is_completed = input("Задача выполнена? (да/нет): ").lower() == "да"

    # Создаём обьект задач и добавляем его в список
    task = Task(task_name, priority, is_completed)
    tasks.append(task)


def display_tasks():
    # Сортировка задач по приоритету
    tasks.sort(key=lambda x: x.priority)

    print("\n--- Список задач ---")
    for task in tasks:
        task.display()


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
