# docker-bind

### Полезное

- [Use bind mounts](https://docs.docker.com/storage/bind-mounts/)

### Задание

1. Вся работа должна выполняться в репозитории `jusan-docker` в папке `docker-bind`.
2. Скачать конфигурационный файл [nginx.conf](./nginx.conf) с помощью `curl`.
3. Запустить контейнер со следующими параметрами:

   - работает на фоне;
   - перенаправляет запрос с хостового порта 7777 на 80 порт контейнера;
   - имя контейнера `jusan-docker-bind`;
   - монтирует скачанный `nginx.conf` внутрь контейнера `/etc/nginx/nginx.conf`;
   - использует образ `nginx:mainline`.

4. Проверьте запрос `http://localhost:7777` с помощью `curl`. В ответ должно прийтие `Привет из Docker контейнера! 🐳`.
5. Посмотрите список запущенных контейнеров. Проверьте в списке, как отображается контейнер `jusan-docker-bind`.
6. Посмотрите на логи `nginx` командой:

```bash
docker logs jusan-docker-bind
```

7. Все выполненные команды в шаге 2 и 3 записать в файл `docker-bind/solution.sh`.

8. Запушить в репозиторий `jusan-docker`. В папке `docker-bind` должны быть:
   - `solution.sh`

В репозитории не должно быть лишних файлов.

Для проверки правильности выполнения текущего задания прикреплен [тестер][tester].

```bash
bash ./tester.sh
```

[tester]: https://stepik.org/media/attachments/lesson/691221/tester-docker-bind.sh

---

### Ответ

ds@ds-HP-ProBook-450-15-6-inch-G9-Notebook-PC:/opt/github/fork_TechOrda/docker/docker-bind$ ls -la
итого 20
drwxr-xr-x  2 root root 4096 Қар 25 16:14 .
drwxr-xr-x 13 root root 4096 Қар 25 16:14 ..
-rw-r--r--  1 root root  769 Қар 25 16:14 nginx.conf
-rw-r--r--  1 root root 1944 Қар 25 16:14 README.md
-rw-r--r--  1 root root 1197 Қар 25 16:14 tester-docker-bind.sh
ds@ds-HP-ProBook-450-15-6-inch-G9-Notebook-PC:/opt/github/fork_TechOrda/docker/docker-bind$ docker run -d --name jusan-docker-bind -p 7777:80 -v ./nginx.conf:/etc/nginx/nginx.conf nginx:mainline 
f7c270124f3b3630a967eaab31c1c702a2d0102dc587865fbaa64ba80f7a4c42
ds@ds-HP-ProBook-450-15-6-inch-G9-Notebook-PC:/opt/github/fork_TechOrda/docker/docker-bind$ docker ps
CONTAINER ID   IMAGE            COMMAND                  CREATED         STATUS         PORTS                                     NAMES
f7c270124f3b   nginx:mainline   "/docker-entrypoint.…"   3 seconds ago   Up 3 seconds   0.0.0.0:7777->80/tcp, [::]:7777->80/tcp   jusan-docker-bind
ds@ds-HP-ProBook-450-15-6-inch-G9-Notebook-PC:/opt/github/fork_TechOrda/docker/docker-bind$ curl http://localhost:7777
Привет из Docker контейнера! 🐳
ds@ds-HP-ProBook-450-15-6-inch-G9-Notebook-PC:/opt/github/fork_TechOrda/docker/docker-bind$ docker logs jusan-docker-bind
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2024/11/25 11:33:26 [notice] 1#1: using the "epoll" event method
2024/11/25 11:33:26 [notice] 1#1: nginx/1.27.2
2024/11/25 11:33:26 [notice] 1#1: built by gcc 12.2.0 (Debian 12.2.0-14) 
2024/11/25 11:33:26 [notice] 1#1: OS: Linux 6.8.0-49-generic
2024/11/25 11:33:26 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1048576:1048576
2024/11/25 11:33:26 [notice] 1#1: start worker processes
2024/11/25 11:33:26 [notice] 1#1: start worker process 29
2024/11/25 11:33:26 [notice] 1#1: start worker process 30
2024/11/25 11:33:26 [notice] 1#1: start worker process 31
2024/11/25 11:33:26 [notice] 1#1: start worker process 32
2024/11/25 11:33:26 [notice] 1#1: start worker process 33
2024/11/25 11:33:26 [notice] 1#1: start worker process 34
2024/11/25 11:33:26 [notice] 1#1: start worker process 35
2024/11/25 11:33:26 [notice] 1#1: start worker process 36
2024/11/25 11:33:26 [notice] 1#1: start worker process 37
2024/11/25 11:33:26 [notice] 1#1: start worker process 38
2024/11/25 11:33:26 [notice] 1#1: start worker process 39
2024/11/25 11:33:26 [notice] 1#1: start worker process 40
2024/11/25 11:33:26 [notice] 1#1: start worker process 41
2024/11/25 11:33:26 [notice] 1#1: start worker process 42
2024/11/25 11:33:26 [notice] 1#1: start worker process 43
2024/11/25 11:33:26 [notice] 1#1: start worker process 44
172.17.0.1 - - [25/Nov/2024:11:33:38 +0000] "GET / HTTP/1.1" 203 52 "-" "curl/8.5.0" "-"
ds@ds-HP-ProBook-450-15-6-inch-G9-Notebook-PC:/opt/github/fork_TechOrda/docker/docker-bind$ bash ./tester-docker-bind.sh 
✅
✅
✅
✅

