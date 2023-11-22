# Лабораторная работа №3

## Начало работы
Для выполнения данной лабораторной работы был создан отдельный репозиторий на GitHub ([ссылка на него](https://github.com/al-shimchenko/test)). В него были добавлены файлы из предыдущей лабораторной работы. <br/><br/>
Файл Python
```
import requests

from colorama import Fore

def get_random_joke():
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    if response.status_code == 200:
        data = response.json()
        return f"{data['setup']} - {data['punchline']}"
    else:
        return "Не удалось получить шутку"

if __name__ == "__main__":
    #print(get_random_joke())
    print(Fore.GREEN + get_random_joke())
    
```
Dockerfile
```
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && pip install colorama

COPY . .

ENTRYPOINT ["python", "./joke.py"]
```
requirements.txt
```
requests==2.26.0
```

Также в репозитории была создана директория `.github/workflows`.


## 2. GitHub Actions

Для работы был создан аккаут в Docker Hub, в нём мы создали тестовый репозиторий, куда в дальнейшем загрузится образ. Добавили секреты в репозиторий на GitHub (Actions repository secrets), которые хранят имя пользователя и пароль от аккаунта Docker Hub. <br/><br/>
<img src="img/1.jpg" alt="1.jpg" width="700"> <br/><br/>
Также создали файл push.yml внутри раннее созданной директории .github/workflows. В файле записан код с инструкциями для GitHub Actions. <br/><br/>
<img src="img/2.jpg" alt="2.jpg" width="700"> <br/><br/>
В этом файле происходят следующие действия:

- При каждом push в ветку main репозитория GitHub запускается рабочий процесс с именем Push image to Docker Hub.
- Рабочий процесс состоит из одной задачи, которая выполняется на виртуальной машине Ubuntu.
- Задача содержит три шага:
  - Первый шаг проверяет репозиторий GitHub с помощью действия `actions/checkout@v4`.
  - Второй шаг входит в Docker Hub с помощью действия `docker/login-action@v3`, используя имя пользователя и пароль, сохраненные в секретах репозитория.
  - Третий шаг собирает Docker-образ из Dockerfile, находящегося в корневой папке репозитория, и отправляет его на Docker Hub с помощью действия `docker/build-push-action@v5`.

## 3. Проверка
В разделе Actions появился workflow, тесты на GitHub успешно выполнились.<br/><br/>
<img src="img/4.jpg" alt="4.jpg" width="700">  <br/><br/>
<img src="img/3.jpg" alt="3.jpg" width="700"> <br/><br/>
Action выполнил все шаги, образ успешно загрузился в репозиторий на Dockerhub.<br/><br/>
<img src="img/5.jpg" alt="5.jpg" width="700">  <br/><br/>

Задание выполнено! :tada:
