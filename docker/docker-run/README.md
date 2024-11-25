# docker-run

Задания в данном модуле будут проверяться ментором в конце модуля.

Для сдачи данного модуля создайте репозиторий в ([ССЫЛКА GITHUB CLASSROOM]).

### Полезное

- [Установка Docker](https://docs.docker.com/get-docker/)

### Задание

1. Установить Docker, если еще не установлен на вашем компьютере.
2. Запустить контейнер на порту `8888` из официального образа `nginx`:

```bash
docker run -d --name jsn-dkr-run -p 8888:80 nginx:mainline
```

3. Вывести список активных контейнеров:

```bash
docker ps
```

4. Проверьте запрос на `http://localhost:8888` с помощью `curl`. Должно появиться приветственное сообщение от `nginx`.
5. Остановить запущенный контейнер:

```bash
docker stop jsn-dkr-run
```

6. Вывести список активных контейнеров, чтобы убедиться что нашего контейнера нет в списке.
7. Проверьте запрос `http://localhost:8888` с помощью `curl`. Должна появиться ошибка, так как наш контейнер был остановлен.
8. Вывести список всех контейнеров. В нем должен появиться наш остановленный контейнер.

```bash
docker ps -a
```

9. Все выполенные команды `docker` записать в репозиторий в файл `docker-run/solution.sh`. В скрипте не должно быть команд `curl`.
   Запушить в гит.

В репозитории не должно быть лишних файлов.

Для проверки правильности выполнения текущего задания прикреплен [тестер][tester].

```bash
bash ./tester.sh
```

[tester]: https://stepik.org/media/attachments/lesson/691221/tester-docker-run.sh

---

### Ответ
ds@ds-HP-ProBook-450-15-6-inch-G9-Notebook-PC:/opt/github/fork_TechOrda/docker/docker-run$ docker run -d --name jsn-dkr-run -p 8888:80 nginx:mainline
Unable to find image 'nginx:mainline' locally
mainline: Pulling from library/nginx
2d429b9e73a6: Already exists 
9b1039c85176: Pull complete 
9ad567d3b8a2: Pull complete 
773c63cd62e4: Pull complete 
1d2712910bdf: Pull complete 
4b0adc47c460: Pull complete 
171eebbdf235: Pull complete 
Digest: sha256:bc5eac5eafc581aeda3008b4b1f07ebba230de2f27d47767129a6a905c84f470
Status: Downloaded newer image for nginx:mainline
3dd45a4d52a989dca852f6973734a4c01bb13672da9d2c7164260a3db91c430e
ds@ds-HP-ProBook-450-15-6-inch-G9-Notebook-PC:/opt/github/fork_TechOrda/docker/docker-run$ docker ps
CONTAINER ID   IMAGE            COMMAND                  CREATED          STATUS          PORTS                                     NAMES
3dd45a4d52a9   nginx:mainline   "/docker-entrypoint.…"   46 seconds ago   Up 45 seconds   0.0.0.0:8888->80/tcp, [::]:8888->80/tcp   jsn-dkr-run
ds@ds-HP-ProBook-450-15-6-inch-G9-Notebook-PC:/opt/github/fork_TechOrda/docker/docker-run$ curl http://localhost:8888
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
ds@ds-HP-ProBook-450-15-6-inch-G9-Notebook-PC:/opt/github/fork_TechOrda/docker/docker-run$ docker stop jsn-dkr-run
jsn-dkr-run
ds@ds-HP-ProBook-450-15-6-inch-G9-Notebook-PC:/opt/github/fork_TechOrda/docker/docker-run$ docker ps -a
CONTAINER ID   IMAGE                         COMMAND                  CREATED              STATUS                     PORTS     NAMES
3dd45a4d52a9   nginx:mainline                "/docker-entrypoint.…"   About a minute ago   Exited (0) 5 seconds ago             jsn-dkr-run
ds@ds-HP-ProBook-450-15-6-inch-G9-Notebook-PC:/opt/github/fork_TechOrda/docker/docker-run$ bash ./tester.sh
bash: ./tester.sh: Нет такого файла или каталога
ds@ds-HP-ProBook-450-15-6-inch-G9-Notebook-PC:/opt/github/fork_TechOrda/docker/docker-run$ bash ./
README.md             tester-docker-run.sh  
ds@ds-HP-ProBook-450-15-6-inch-G9-Notebook-PC:/opt/github/fork_TechOrda/docker/docker-run$ bash ./tester-docker-run.sh 
✅
✅
✅

