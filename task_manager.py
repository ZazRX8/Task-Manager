# Ввод данных от пользователя
task_name = input("Введите название задачи: ")
priority = int(input("Введите приоритет задачи (число): "))
is_completed = input("Задача выполнена? (да/нет): ").lower() == "да"

# Вывод данных
print("\n--- Информация о задаче ---")
print("Задача: ", task_name)
print("Приоритет: ", priority)
print("Выполнено: ", is_completed)
