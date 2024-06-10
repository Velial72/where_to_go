# Куда пойти - места Москвы

- [Демо сайта](http://anton664.pythonanywhere.com/)
- [Панель администратора](http://anton664.pythonanywhere.com/admin)


Сайт о самых интересных местах Москвы.

![Скриншот главной страницы]()


## HКак добавить новую локацию

- Открой [панель администратора](http://anton664.pythonanywhere.com/admin)
- В левой колонке выберите `Место`
- Ты можешь добавить новую локацию и отредактировать существующие

## Как запустить

Python3 должен быть установлен. Версия не ниже `3.11`.<br>

Проверь версию Python:
```
python3 --version
```

Затем используйте `pip` для установки зависимостей:
```
pip install -r requirements.txt
```

* Скопируй код с [GitHub]()

    Перед запуском необходимо настроить переменные среды. Создай файл ".env" со следующим содержимым:

    ```
    SECRET_KEY=<put here your secret key>
    ALLOWED_HOSTS=localhost,127.0.0.1,<add here your website address>
    DEBUG=<set False for development and True for production>
    ```

* Помести все статические файлы (js, css, изображения и т.д.) в ресурсы, а затем собери все статические файлы в статический тип:
    ```
    python3 manage.py collectstatic
    ```

* Выполни миграцию базы данных:
    ```
    python3 manage.py makemigrations places
    python3 manage.py migrate
    ```

* Запусти сервер используя `manage.py`
    ```
    python3 manage.py runserver
    ```

*  В браузере открой страницу с данными по следующему адресу: `127.0.0.1:8000".

## Тестовые данные

Для загрузки новых локаций используй команду и ссылку на данные как в примере "sample_place_file.json":

```
python manage.py load_place http://example.com/sample_place_file.json
```

Также вы можете передать несколько адресов сразу.
