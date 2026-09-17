import json
import os

DATA_FILE = "tasks.json"


def load_tasks():
    """Загружает задачи из файла."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    """Сохраняет задачи в файл."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def add_task(tasks, title):
    """Добавляет новую задачу."""
    task = {"id": len(tasks) + 1, "title": title, "done": False}
    tasks.append(task)
    print(f"Добавлено: {title}")


def list_tasks(tasks):
    """Показывает все задачи."""
    if not tasks:
        print("Список пуст.")
        return
    for t in tasks:
        mark = "✔" if t["done"] else "✘"
        print(f"[{mark}] {t['id']}. {t['title']}")

def mark_undone(tasks, task_id):
    """Снимает отметку выполнения."""
def find_task(tasks, task_id):
    """Находит задачу по id. Возвращает словарь или None."""
    for t in tasks:
        if t["id"] == task_id:
            return t
    return None


def mark_done(tasks, task_id):
    """Отмечает задачу выполненной."""
    task = find_task(tasks, task_id)
    if not task:
        print(f"Задача {task_id} не найдена.")
        return
    task["done"] = False
    save_tasks(tasks)
    print(f"Возвращено в работу: [{task_id}] {task['title']}")
    task["done"] = True
    save_tasks(tasks)
    print(f"Выполнено: [{task_id}] {task['title']}")


def delete_task(tasks, task_id):
    """Удаляет задачу по id."""
    task = find_task(tasks, task_id)
    if not task:
        print(f"Задача {task_id} не найдена.")
        return
    tasks.remove(task)
    save_tasks(tasks)
    print(f"Удалено: [{task_id}] {task['title']}")
    
def main():
    tasks = load_tasks()

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