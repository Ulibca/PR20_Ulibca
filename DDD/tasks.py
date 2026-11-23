import json
import os


def add_task(tasks, title, minutes):
    title = title.strip()
    minutes = int(minutes)

    if title == '' or minutes <= 0:
        raise ValueError('Ошибочка')

    task = {
        "title": title,
        "minutes": minutes,
        "done": False
    }
    tasks.append(task)
    return tasks


def total_minutes(tasks, only_active=True):
    total = 0
    for task in tasks:
        if only_active == True:
            if not task['done']:
                total += task['minutes']
        else:
            total += task['minutes']
    return total


def complete_task(tasks, index):
    if index < 0 or index >= len(tasks):
        raise IndexError("Ошибочка!")
    tasks[index]['done'] = True
    return tasks


def save_tasks(tasks, filepath="tasks.json"):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def load_tasks(filepath="tasks.json"):
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)