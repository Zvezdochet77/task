# Order API Practice

Учебный проект: проектирование API-метода для экрана с данными о заказе.

Есть дизайн экрана и структура БД, в которой информация распределена между таблицами заказов, пользователей, товаров и статусов. Задача — спроектировать JSON-ответ метода, который одновременно учитывает потребности UI, структуру данных и дальнейшую реализацию.

## Что нужно определить

- какие данные должны попасть в JSON;
- из каких таблиц и полей их получать;
- как назвать поля;
- какие типы данных использовать;
- где нужен вложенный объект, а где — массив;
- передавать идентификатор или полный объект;
- какие поля сделать обязательными.

## Стек

- Python
- [FastAPI](https://fastapi.tiangolo.com/) + Uvicorn
- SQLAlchemy (SQLite, файл `test.db`)
- Pydantic — схемы запросов и ответов

## Структура проекта

| Файл | Назначение |
|------|------------|
| `main.py` | Точка входа, приложение FastAPI |
| `database.py` | Подключение к БД, сессия, `get_db` |
| `models.py` | Модели SQLAlchemy |
| `schemas.py` | Pydantic-схемы для JSON |
| `requirements.txt` | Зависимости |

## Структура БД

| Таблица | Поля |
|---------|------|
| `users` | `id`, `full_name`, `email`, `phone` (nullable) |
| `order_statuses` | `id`, `code` (unique), `title` |
| `products` | `id`, `title`, `price` (Numeric 10,2) |
| `orders` | `id`, `user_id` → `users.id`, `status_id` → `order_statuses.id` |
| `order_items` | `order_id` → `orders.id`, `product_id` → `products.id`, `quantity` (составной PK) |

Связи: заказ принадлежит одному пользователю и имеет один статус; заказ и товары связаны «многие ко многим» через `order_items` с количеством.

## Схемы JSON (`schemas.py`)

- `UserRead` — вложенный объект пользователя (`id`, `full_name`, `email`, `phone`).
- `OrderStatusRead` — вложенный объект статуса (`id`, `code`, `title`).
- `OrderItemRead` — позиция заказа (`product_id`, `title`, `price`, `quantity`, `total`); позиции идут массивом.
- `OrderDetailResponse` — ответ метода: `id`, `user`, статус, `items`, `total`.
- `OrderCreate` — тело запроса на создание заказа: `user_id` и список позиций.

Пример ответа:

```json
{
  "id": 1,
  "user": {
    "id": 10,
    "full_name": "Иван Иванов",
    "email": "ivan@example.com",
    "phone": "+79990000000"
  },
  "status": {
    "id": 2,
    "code": "paid",
    "title": "Оплачен"
  },
  "items": [
    {
      "product_id": 5,
      "title": "Клавиатура",
      "price": 3500.00,
      "quantity": 2,
      "total": 7000.00
    }
  ],
  "total": 7000.00
}
```

## Запуск

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Статус

Модели и схемы описаны, эндпоинты в `main.py` пока не реализованы.
