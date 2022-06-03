**Концепция**

Сайт посвящен онлайн-образованию. Главными функциями являются трансляции лекций и задачи по блокам.

**ToDo**

- Трансляции в реальном времени ~~с чатом~~
- Уведомление о начале занятия на почту
- Рекомндации курсов
- Техническая поддержка
- Распределение учеников на группы
- Сбор интересов ученика для более качественной подборки курсов
- Успеваемость
- Репетиторы

Пример сайта на который мы ориентируемся - https://foxford.ru/.

**Работа с проектом**

Для начала работы создайте новый каталог и введите следущие команды:

``python3 -m venv venv``

``pip install --upgrade pip``

``pip install django==4.0``

``source ./venv/bin/activate``

``git clone https://github.com/andonlya/edutech.git``

``cd edutech/EduTech``

``python3 manage.py makemigrations``

``python3 manage.py migrate``

``python3 manage.py runserver``

