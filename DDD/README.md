# Локальный трекер задач (Практическая работа № 20)

Консольное приложение на Python для учёта учебных и рабочих задач с сохранением данных в формат JSON.

## Подготовка и запуск окружения (Windows PowerShell)

1. Создание виртуального окружения:
   ```powershell
   python -m venv .venv
   ```

2. Активация окружения и установка зависимостей:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
   ```

## Запуск программы
```powershell
python main.py
```

## Запуск автоматических тестов
```powershell
python -m unittest -v
```
