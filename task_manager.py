# task_manager.py

from datetime import datetime


class Task:
    def __init__(self, title, description, priority, due_date, completed=False):
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = completed
        self.due_date = due_date

    def display(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        due_date_str = self.due_date.strftime("%Y-%m-%d")
        print(f"Задача: {self.title}")
        print(f"Описание: {self.description}")
        print(f"Приоритет: {self.priority}")
        print(f"Дата выполнения: {due_date_str}")
        print(f"Статус: {status}\n")


tasks = []


def add_task():
    title = input("Введите название задачи: ")
    description = input("Введите описание задачи: ")
    priority = int(
        input("Введите приоритет задачи (1 - высокий, 2 - средний, 3 - низкий): "))
    due_date_str = input(
        "Введите дату выполнения задачи (в формате ГГГГ-ММ-ДД): ")
    due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
    is_completed = input("Задача выполнена? (да/нет): ").lower() == "да"

    task = Task(title, description, priority, due_date, is_completed)
    tasks.append(task)


def display_tasks():
    tasks.sort(key=lambda x: (x.priority, x.due_date))
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
