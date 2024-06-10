<h1 align='center'>API Форума рецептов</h1>

Проект представляет собой форум рецептов сделанный с использованием технологии Django Rest Framework. В проекте реализован весь CRUD, авторизация(использовалась библиотека djoser)



### API Endpoint

#### Authentication

* **/auth/users/** (Регистрация пользователя)
* **/auth/token/login/** (Авторизация пользователя)
* **/api/users/logout/** (Выход пользователя)


#### Users

* **/recipe_api/user_lc/** (Вывод всех пользователей 'GET', Добавление пользователя 'POST')
* **/recipe_api/user_lc/?login** (Поиск пользователя по лоигну 'GET')
* **/recipe_api/user_detail/pk/** (Чтение пользователя 'GET', Редактирование пользователя 'PUT', Удаление пользователя 'DELETE')
  

#### Recipe

* **/recipe_api/recipe_list/** (Вывод всех пользователей 'GET')
* **/recipe_api/recipe_list/?title=&category=&order_by** (Поиск рецепта по названию, Сортировка по категории, Сортировка по рейтингу и дате 'GET')
* **/recipe_api/recipe_create/** (Добавление рецепта 'POST')
* **/recipe_api/recipe_detail/pk/** (Чтение рецепта 'GET', Редактирование рецепта 'PUT', Удаление пользователя 'DELETE')


#### Category

* **/recipe_api/catlist/** (Вывод всех категорий 'GET')
* **/recipe_api/recipe_create/** (Добавление категории 'POST')
* **/recipe_api/recipe_detail/pk/** (Чтение категории 'GET', Редактирование категории 'PUT', Удаление категории 'DELETE')


#### Comment

* **/recipe_api/comment_list/** (Вывод всех комментариев 'GET')
* **/recipe_api/comment_list/?order_by=comment_posted_at** (Сортировка по дате и рейтингу 'GET')
* **/recipe_api/comment_create/** (Добавление комментария 'POST')
* **/recipe_api/comment_detail/pk/** (Чтение комментария 'GET', Редактирование комментария 'PUT', Удаление комментария 'DELETE')


### Install 

    pip install -r req.txt

### Usage

    python manage.py test

### License

  Этот проект лицензирован под MIT License.


    

