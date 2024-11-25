# docker-exec-theory

В данном уроке мы разберем, как запускать команды внутри Docker контейнера.

В первом уроке, мы узнали, что контейнеры имеют много общего с виртуальными машинами.
Контейнер внутри имеет свою операционную систему. В этой операционной системе можно
запускать те же команды, что и на обычной ОС.

Для запуска команд внутри контейнера нужно использовать команду `docker exec`.

Пример запуска команды внутри контейнера:

```bash
docker exec jusan-docker-bind ls
```

Команда выше вызывает `ls` внутри контейнера `jusan-docker-bind`.

Команда `docker exec` используется в следующих случаях:

- Разовый запуск команды в контейнере. Например, отправка сигнала сервису в контейнере.
- Получение доступа к терминалу контейнера. В таком терминале все запущенные команды вызываются в контейнере.
  На stepik.org заданиях по Linux, когда вы работали на сервере, на самом деле вы работали в контейнере.

У команды `docker exec` есть два наиболее часто используемых параметров.

<table>
<tr>
    <th>Параметр</th>
    <th>Описание</th>
</tr>
<tr>
    <td>-i</td>
    <td>
        Название флага исходит от слова "interactive", в переводе "интерактивный".<br>
        Запускает команду в интерактивном режиме, т.е. пользователь может непрерывно<br>
        вводить в консоль, если есть такая возможность.
    </td>
</tr>
<tr>
    <td>-t</td>
    <td>
        Название флага исходит от слова "tty", значит "терминал".<br>
        Запускат оболочку псевдо-терминала.
    </td>
</tr>
</table>

> 💡 Взгяните на все доступные параметры `docker exec --help`

### Примеры использования

Если хотите запустить команду, которая что-то выводит, либо передает какой-то сигнал внутри контейнера,
то запускайте `docker exec` без всяких флагов.

Например, как в примере выше, запуск `ls`, не требует интерактивности и псевдо-терминала.

```bash
docker exec jusan-docker-bind ls
```

А вот, если хотите получить доступ к терминалу внутри контейнера, то нужно использовать
параметры `-i` и `-t` вместе.

```bash
docker exec -it jusan-docker-bind bash
```

Флаги `-i` и `-t` можно объединить в `-it`. Так можно делать во многих командах Linux.

> 🕹 Попробуйте получить доступ в терминал контейнера и поиграться в нем.

ds@ds-HP-ProBook-450-15-6-inch-G9-Notebook-PC:/opt/github/fork_TechOrda/docker/docker-exec-theory$ docker exec jusan-docker-bind ls
bin
boot
dev
docker-entrypoint.d
docker-entrypoint.sh
etc
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
ds@ds-HP-ProBook-450-15-6-inch-G9-Notebook-PC:/opt/github/fork_TechOrda/docker/docker-exec-theory$ docker exec -it jusan-docker-bind bash
root@f7c270124f3b:/# ls -la
total 72
drwxr-xr-x   1 root root 4096 Nov 25 11:33 .
drwxr-xr-x   1 root root 4096 Nov 25 11:33 ..
-rwxr-xr-x   1 root root    0 Nov 25 11:33 .dockerenv
lrwxrwxrwx   1 root root    7 Nov 11 00:00 bin -> usr/bin
drwxr-xr-x   2 root root 4096 Oct 31 11:04 boot
drwxr-xr-x   5 root root  340 Nov 25 11:33 dev
drwxr-xr-x   1 root root 4096 Nov 12 02:03 docker-entrypoint.d
-rwxr-xr-x   1 root root 1620 Nov 12 02:02 docker-entrypoint.sh
drwxr-xr-x   1 root root 4096 Nov 25 11:33 etc
drwxr-xr-x   2 root root 4096 Oct 31 11:04 home
lrwxrwxrwx   1 root root    7 Nov 11 00:00 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Nov 11 00:00 lib64 -> usr/lib64
drwxr-xr-x   2 root root 4096 Nov 11 00:00 media
drwxr-xr-x   2 root root 4096 Nov 11 00:00 mnt
drwxr-xr-x   2 root root 4096 Nov 11 00:00 opt
dr-xr-xr-x 441 root root    0 Nov 25 11:33 proc
drwx------   2 root root 4096 Nov 11 00:00 root
drwxr-xr-x   1 root root 4096 Nov 25 11:33 run
lrwxrwxrwx   1 root root    8 Nov 11 00:00 sbin -> usr/sbin
drwxr-xr-x   2 root root 4096 Nov 11 00:00 srv
dr-xr-xr-x  13 root root    0 Nov 25 11:33 sys
drwxrwxrwt   2 root root 4096 Nov 11 00:00 tmp
drwxr-xr-x   1 root root 4096 Nov 11 00:00 usr
drwxr-xr-x   1 root root 4096 Nov 11 00:00 var
