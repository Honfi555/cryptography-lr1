# Лабораторная работа №1


## Включает шифры:
- Цезаря
- Линейный
- Перестановок


## Переменные среды
Для создания .env файла выполните команду:
```bash
    cp .env.example .env
```

### Общие
- SECRET_DATA (str)
- ALFABET_POWER (int) = 1_114_111

### Шифра Цезаря
- OFFSET (int)

### Шифр Перестановки
- PERMUTATION_KEY

### Линейный
- LINEAR_KEY_A (int)
- LINEAR_KEY_B (int)


## Зависимости
Для хранения зависимостей используются файлы pyproject.toml и uv.lock
Установка зависимостей и настройка виртуального окружения:
```bash
  pip install uv
  uv sync
```

## Режим запуска
```bash
    source ./venv/bin/activate
    python3 caesar_cipher.py
```
```bash
    source ./venv/bin/activate
    python3 linear_cipher.py
```
```bash
    source ./venv/bin/activate
    python3 permutation_cipher.py
```
