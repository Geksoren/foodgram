Описание проекта:
Foodgram - это веб-приложение для публикации рецептов, составления списков покупок и подписки на авторов. Проект состоит из: Backend на,Django REST Framework, Frontend на React, База данных PostgreSQL, Nginx в качестве прокси-сервера

Технологии:
Python 3.10

Django 3.2

Django REST Framework

PostgreSQL 13

Docker

Nginx

Запуск проекта (production)
1. Настройка окружения
Создайте файл infra/.env:

DB_ENGINE=django.db.backends.postgresql
DB_NAME=foodgram
POSTGRES_USER=foodgram_user
POSTGRES_PASSWORD=ваш-пароль
DB_HOST=db
DB_PORT=5432

SECRET_KEY=ваш-secret-key
DEBUG=False
2. Сборка и запуск контейнеров
bash
docker-compose -f infra/docker-compose.yml build
docker-compose -f infra/docker-compose.yml up -d
3. Применение миграций
bash
docker-compose -f infra/docker-compose.yml exec backend python manage.py migrate
docker-compose -f infra/docker-compose.yml exec backend python manage.py collectstatic 
Доступ к приложению
Frontend: http://localhost

API: http://localhost/api/

Документация API: http://localhost/api/docs/

Админка: http://localhost/admin/

Использование API
Примеры запросов:

Получение списка рецептов:

GET /api/recipes/
Создание рецепта:

POST /api/recipes/
Headers: Authorization: Token ваш-токен
Body:
{
  "name": "Название",
  "ingredients": [{"name": "ингредиент", "amount": 100}],
  "tags": [1, 2],
  "image": "data:image/png;base64,...",
  "text": "Описание",
  "cooking_time": 30
}

Автор
Левченко Наталья