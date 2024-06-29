<h2>Интернет-магазин мебели "Интерьер"</h2>
Создание интернет-магазина на основе ранее созданной верстки

<h3>Установка:</h3>
<h4>1. Создать пользователя на PostgreSQL:</h4>
    Логин: interior<br>
    Пароль: 1
<h4>2. Создать базу данных interior с владельцем созданного пользователя (обязательно)</h4>

<h4>3. Клонируем репозиторий</h4>
<code>git clone https://github.com/troxin-a/interior-furniture-store.git</code><br>
<code>cd interior-furniture-store</code></code><br>

<h4>4. Устанавливаем зависимости</h4>
<code>poetry shell</code><br>
<code>poetry install</code><br>

<h4>5. Создаем таблицы в базе данных</h4>
<code>cd app</code><br>
<code>python3 manage.py migrate</code><br>

<h4>6. Создаем администратора сайта:</h4>
<code>python3 manage.py createsuperuser</code><br>

<h4>7. Наполним базу данных несколькими товарами из файла</h4>
<code>python3 manage.py loaddata fixtures/goods/cats.json</code><br>
<code>python3 manage.py loaddata fixtures/goods/prods.json</code><br>

<h4>8. Запускаем!</h4>
<code>python3 manage.py runserver</code><br>

Готово! Сайт находится по адресу http://localhost:8000.<br>
Админ-панель для добавления товара (ссылка на главной странице) доступна только под админом сайта