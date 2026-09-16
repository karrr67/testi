import json
import os

DATA_FILE = "tasks.json"


def add_task(tasks, title):
    task = {"id": len(tasks) + 1, "title": title, "done": False}
    tasks.append(task)
    print(f"Добавлено: {title}")


def list_tasks(tasks):
    if not tasks:
        print("Список пуст.")
        return
    for t in tasks:
        mark = "✔" if t["done"] else "✘"
        print(f"[{mark}] {t['id']}. {t['title']}")

def main():

    while True:
        print("\n1. Показать  2. Добавить  3. Выход")
        choice = input("Выбор: ").strip()

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            title = input("Что добавить: ").strip()
            add_task(tasks, title)
            save_tasks(tasks)
        elif choice == "3":
            break
        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    main()