from tasks import add_task, total_minutes, complete_task, save_tasks, load_tasks


def main():
    filepath = "tasks.json"
    tasks = load_tasks(filepath)

    while True:
        print("\n--- МЕНЮ ---")
        print("1 - Добавить задачу")
        print("2 - Показать все задачи")
        print("3 - Отметить задачу выполненной")
        print("4 - Показать остаток минут")
        print("0 - Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            title = input("Введите название задачи: ")
            minutes_str = input("Введите время в минутах: ")
            try:
                minutes = int(minutes_str)
                add_task(tasks, title, minutes)
                save_tasks(tasks, filepath)
                print("Задача успешно добавлена.")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "2":
            if not tasks:
                print("Список задач пуст.")
            else:
                print("\nСписок задач:")
                for i, task in enumerate(tasks, start=1):
                    status = "[x]" if task["done"] else "[ ]"
                    print(f"{i}. {status} {task['title']} ({task['minutes']} мин.)")

        elif choice == "3":
            if not tasks:
                print("Список задач пуст.")
                continue
            num_str = input("Введите номер выполненной задачи: ")
            try:
                index = int(num_str) - 1
                complete_task(tasks, index)
                save_tasks(tasks, filepath)
                print("Задача отмечена выполненной.")
            except (ValueError, IndexError):
                print("Ошибка: введите корректный номер задачи из списка.")

        elif choice == "4":
            mins = total_minutes(tasks, only_active=True)
            print(f"Осталось минут по активным задачам: {mins}")

        elif choice == "0":
            save_tasks(tasks, filepath)
            print("Данные сохранены. Выход из программы.")
            break

        else:
            print("Неизвестная команда. Выберите пункт от 0 до 4.")


if __name__ == "__main__":
    main()