# Аналог Яндекс Афиши

Этот проект представляет аналог Яндекс Афиши.

Ссылка на демонстрацию: https://natewentworth.pythonanywhere.com/

## Установка

Необходимо иметь установленный [Python 3.12+](https://www.python.org/downloads/release/python-3125/)

Скопируйте следующую команду и вставьте в терминал, чтобы скопировать проект:

```
git clone https://github.com/abfalex/yandex_afisha.git
```

Теперь необходимо создать файл `.env` в корне проекта, указав несколько значений в форме `ПЕРЕМЕННАЯ=значение`:

| Параметр        | Описание                                                                                           |
|-----------------|----------------------------------------------------------------------------------------------------|
| `SECRET_KEY`    | Секретный ключ для криптографических операций в Django. Используется для подписывания токенов, паролей и других компонентов. |
| `ALLOWED_HOSTS` | Список доменов или IP-адресов, с которых можно получить доступ к Django приложению.                 |
| `DEBUG`         | Режим отладки. При значении `True` отображаются подробные ошибки при возникновении исключений.      |
| `DB_NAME`       | Название базы данных, используемой приложением Django. Это имя, под которым создается и управляется база данных. |


Необходимо заменить значение этих данных на свои.

Далее вам необходимо создать виртуальную среду для удобного использования (рекомендуется):

```
python -m venv <venv_name>
```

После установки виртуальной среды ее необходимо активировать:

- В Windows:

    ```
    <venv_name>\Scripts\activate
    ```

- В macOS и Linux:

    ```
    source <venv_name>/bin/activate
    ```

После вам необходимо установить необходимые библиотеки. Введите эту команду в терминал:

```
pip install -r requirements.txt
```

## Запуск
Введите следующую команду в терминал, чтобы запустить проект:

```
python3 manage.py runserver
```

После этого, вам необходимо перейти по адресу [127.0.0.1:8000](https://127.0.0.1:8000).

Для управления локациями необходимо перейти по следующему адресу:
 [127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).

### Загрузка данных
Для удобной загрузки данных необходимо использовать следующую команду:

```
python3 manage.py load_place -u <URL на JSON>
```

Замените `<>` на ссылку с json данными.

Образец JSON файла локации:

```
{
    "title": "название локации",
    "imgs": [
        "ссылка на изображение",
        ...
    ],
    "description_short": "короткое описание",
    "description_long": "подробное описание",
    "coordinates": {
        "lng": "долгота",
        "lat": "широта"
    }
}
```