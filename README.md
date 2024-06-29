Интернет-магазин мебели "Интерьер"

1. Создать пользователя на PostgreSQL:
    Логин: interior
    Пароль: 1
2. Создать базу данных interior с владельцем созданного пользователя (обязательно)

3. Клонируем репозиторий
git clone https://github.com/troxin-a/interior-furniture-store.git
cd interior-furniture-store

4. Устанавливаем зависимости
poetry shell
poetry install

5. Создаем таблицы в базе данных
cd app
python3 manage.py migrate

6. Создаем администратора сайта:
python3 manage.py createsuperuser

7. Наполним базу данных несколькими товарами из файла
python3 manage.py loaddata fixtures/goods/cats.json
python3 manage.py loaddata fixtures/goods/prods.json

8. Т.к. изображения товаров уже ссылаются на определенные файлы, их тоже нужно добавить.
Поместим папку media рядом с остальными папками: app, cats, fixtures, goods и т.д.

9. Запускаем!
python3 manage.py runserver

Готово! Сайт находится по адресу http://localhost:8000.
Админ-панель для добавления товара (ссылка на главной странице) доступна только под админом сайта

