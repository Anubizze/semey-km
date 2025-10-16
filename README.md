# Semey-KM Factory Management System

[![CI/CD Pipeline](https://github.com/Anubizze/semey-km/actions/workflows/ci.yml/badge.svg)](https://github.com/Anubizze/semey-km/actions/workflows/ci.yml)

Система управления производством для керамического завода с отслеживанием партий, материалов и оборудования.

## Возможности

- 🔐 Авторизация и разграничение прав доступа (администратор, директор, оператор автоклава, резчик)
- 📦 Управление партиями продукции
- 🧱 Учёт материалов и их расход
- 🏭 Мониторинг оборудования (автоклавы)
- 📊 Отчётность и экспорт в Excel
- 🎯 Шаблоны партий для быстрого создания
- ⚡ Кэширование для оптимизации производительности

## Требования

- Python 3.9+
- SQLite
- Flask и зависимости (см. `requirements.txt`)

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Anubizze/semey-km.git
cd semey-km
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
```

3. Активируйте виртуальное окружение:
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

4. Установите зависимости:
```bash
pip install -r requirements.txt
```

5. Инициализируйте базу данных:
```bash
python init_all_data.py
```

6. Создайте администратора:
```bash
python create_admin.py
```

## 🚀 Деплой и запуск

### Render.com (Рекомендуется)

Render - простой и надежный способ развернуть ваше приложение в облаке:

1. **Перейдите на [render.com](https://render.com)** и зарегистрируйтесь
2. **Подключите GitHub**: 
   - Нажмите "New +" → "Web Service"
   - Подключите GitHub аккаунт
   - Выберите репозиторий `semey-km`
3. **Настройте сервис**:
   - **Name**: `semey-km-factory`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python init_all_data.py && python create_admin.py && python app.py`
4. **Настройте переменные окружения**:
   - `FLASK_ENV=production`
   - `SECRET_KEY=your-super-secret-key-here`
5. **Нажмите "Create Web Service"** 🚀

**Ваше приложение будет доступно по URL вида:** `https://semey-km-factory.onrender.com`

### Локальная разработка

Для разработки локально:

```bash
# Windows
start_server.bat

# Linux/Mac  
python app.py
```

Приложение будет доступно по адресу: `http://127.0.0.1:5000`

## Структура проекта

```
semey-km/
├── app.py                 # Основное Flask-приложение
├── models.py              # Модели базы данных (SQLAlchemy)
├── templates/             # HTML-шаблоны
├── static/                # Статические файлы (CSS, JS, изображения)
├── instance/              # База данных (не в git)
├── init_all_data.py       # Инициализация БД с тестовыми данными
├── create_admin.py        # Создание администратора
├── check_products.py      # Проверка продуктов
├── test_system.py         # Тесты системы
└── requirements.txt       # Зависимости Python
```

## Пользователи по умолчанию

После инициализации доступны следующие аккаунты:

- **Администратор**: `admin` / `admin123`
- **Директор**: `director` / `director123`
- **Оператор автоклава**: `autoclave_op` / `autoclave123`
- **Резчик**: `cutter_op` / `cutter123`

## Роли и права доступа

| Роль | Возможности |
|------|-------------|
| **Администратор** | Полный доступ: управление пользователями, партиями, оборудованием |
| **Директор** | Просмотр отчётов, экспорт данных, мониторинг производства |
| **Оператор автоклава** | Управление автоклавами, просмотр партий |
| **Резчик** | Работа с операциями резки |

## Тестирование

Запустите тесты:
```bash
python test_system.py
```

## CI/CD

Проект использует GitHub Actions для автоматического тестирования при каждом push/PR в ветку `main`. Конфигурация: `.github/workflows/ci.yml`

## Лицензия

Проприетарное программное обеспечение

## Деплой

🌐 **Live Demo**: [https://semey-km-factory.onrender.com](https://semey-km-factory.onrender.com)

🚀 **Hosted on**: [Render.com](https://render.com)

## Контакты

- GitHub: [@Anubizze](https://github.com/Anubizze)
- Repository: [semey-km](https://github.com/Anubizze/semey-km)

