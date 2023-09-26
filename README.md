# DjangoBot
## Схема работы
```
1. создаем нового пользователя
2. получаем access jwt token ( срок жизни токена 1 день)
3. заходим в телеграм бота и получаем номер пользователя
3. генерируем bot token в кабинете (доступ только по access token и требуется код из телеграм бота.)
4. с помощью bot token отправляем сообщения пользовтелю
```



## Телеграм бот:
```
https://t.me/bigtestobot
```
## Swagger docs:
```
http://188.130.160.216:8000/api/
```

# API документация


## Создание пользователя

**Метод:** POST

**URL:** `http://188.130.160.216:8000/api/user/`

**Тело запроса (JSON):**
```json
{
    "name": "Fedor",
    "login": "FedXL",
    "psw": "password1234"
}
```

## Изменение имени или пароля пользователя

**Метод:** PUT

**URL:** `http://188.130.160.216:8000/api/user/`

**Тело запроса (JSON):**
```json
{
    "name": "Fedor",
    "login": "FedXL",
    "psw": "password1234"
}
```
**Заголовки:**
```commandline
Authorization:  Bearer AccessToken 
```

## Удаление пользователя

**Метод:** DELETE

**URL:** `http://188.130.160.216:8000/api/user/`

**Тело запроса (JSON):**
```json
{
    "name": "Fedor",
    "login": "FedXL",
    "psw": "password1234"
}
```
**Заголовки:**
```commandline
Authorization:  Bearer AccessToken 
```
**Ответ (JSON):**
```json
{"answer":"success user was deleted"}
```


## Авторизация Получение AccessToken 

**Метод:** POST

**URL:** `http://188.130.160.216:8000/api/auth/`

**Тело запроса (JSON):**
```json
{
    "login": "FedXL",
    "psw": "password1234"
}

```
**Ответ (JSON):**
```json
{
    "answer":"success",
    "access_token":"JwtToken"
}
```

## Получение Bot Token для отправки сообщений боту
**Метод:** POST

**URL:** `http://188.130.160.216:8000/api/cabinet/`

**Тело запроса (JSON) код пользователь получает из телеграм бота:**
```json
{"code":"0001"}
```
**Заголовки:**
```commandline
Authorization:  "Bearer AccessToken" 
```
**Ответ (JSON):**
```json
{
    "answer": "success",
    "bot_token": "PD1B0WwEmdVQIc7SzfKFUQrPH"
}
```

## Получение истории сообщений
**Метод:** GET

**URL:** `http://188.130.160.216:8000/api/cabinet`


**Заголовки:**
```commandline
Authorization:  "Bearer AccessToken" 
```
**Ответ (JSON):**
```json
{
  "answer": "success",
  "messages": [
    {
      "time": "2023-09-25T02:47:11.305832Z",
      "text": "some and again text",
      "type": "Text"
    },
    {
      "time": "2023-09-25T02:46:57.071136Z",
      "text": "some another text",
      "type": "Text"
    },
    {
      "time": "2023-09-25T02:46:48.940847Z",
      "text": "some text",
      "type": "Text"
    }
  ]
}  
      
```

## Отправка сообщений телеграм боту
**Метод:** POST

**URL:** `http://188.130.160.216:8000/api/send_message`

**Тело запроса (JSON) :**
```json
{
    "text":"some and again text",
    "type":"Text",
    "bot_token":"7EVgXzmREWIf1qHsaYkegiQMa"
}
```
**Ответ (JSON):**
```json
{
    "answer": "message was successfully send"
}
```

