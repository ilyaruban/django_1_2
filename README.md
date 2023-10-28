# Домашнее задание по теме "Обработка запросов и шаблоны"

## Задание

Ваша задача — написать простой сервис-помощник для приготовления блюд.

Сервис знает некоторое количество рецептов (см. файл `calculator/views.py` —- переменная `DATA`).

На запрос вида `/omlet/` должен отобразиться список ингредиентов и их количество для приготовления омлета. Аналогично для запроса вида `/pasta/` — список ингредиентов и их количество для приготовления макарон с сыром. И т. д.

Например:

```
http://127.0.0.1:8000/omlet/

# Ответ
яйца, шт: 2
молоко, л: 0.1
соль, ч.л.: 0.5
```

По умолчанию сервис сообщает количество ингредиентов на одну порцию. Но если передать опциональный параметр `servings` (целое положительное число), то сервис должен выдать количество ингредиентов на указанное число порций.

Например:

```
http://127.0.0.1:8000/omlet/?servings=4

# Ответ
яйца, шт: 8
молоко, л: 0.4
соль, ч.л.: 2.0
```