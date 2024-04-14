## Концепция

Онлайн-образовательная платформа на Django и SQLite с функциями трансляции лекций и выполнения заданий. Используется встроенный плеер YouTube.

## Основные функции

- Главная страница с общей информацией
- Страница курсов для просмотра предложений
- Регистрация и аутентификация пользователей
- Личный профиль для управления данными
- Страница трансляций лекций
- Подробности курсов с дополнительными материалами

Сайт, к которому мы стремимся: [Фоксфорд](https://foxford.ru/).

## Настройка проекта

1. Настройка окружения и установка Django:
   ```bash
   python3 -m venv venv
   source ./venv/bin/activate
   pip install --upgrade pip
   pip install django==4.0
   ```
2. Клонирование проекта и настройка базы данных:
   ```bash
   git clone https://github.com/IlyaKataev/edutech.git
   cd edutech/EduTech
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```
3. Запуск сервера:
   ```bash
   python3 manage.py runserver
   ```

Доступ к сайту по адресу [http://localhost:8000](http://localhost:8000)
