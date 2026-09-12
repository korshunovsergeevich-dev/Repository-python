# Автоматизированные тесты UI (Selenium + Pytest + Allure)

Проект содержит набор автотестов для проверки функциональности веб-приложений (на примере SauceDemo и калькулятора).  
Тесты используют связку **Selenium WebDriver**, **Pytest** и систему отчётов **Allure**.

## Требования к окружению

Для работы проекта необходимо:

*   **Python** версии 3.8 или выше.
*   **Google Chrome** (браузер должен быть установлен в системе).
*   **Allure Commandline** (для генерации отчётов).
*   **Виртуальное окружение** (рекомендуется для изоляции зависимостей).

---

## Установка зависимостей

1.  Создайте и активируйте виртуальное окружение:
    ```bash
    # Windows (PowerShell)
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1

    # Windows (cmd)
    python -m venv .venv
    .\.venv\Scripts\activate.bat

    # macOS / Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

2.  Установите необходимые пакеты из файла `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

---

## Как запустить тесты и сформировать отчёт

Для запуска тестов и сбора данных для отчёта выполните следующую команду в терминале (находясь в корне проекта):

```bash
pytest --alluredir=allure-results
