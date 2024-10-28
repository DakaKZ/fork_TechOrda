# nginx-install

В данном уроке разберем как правильно устанавливать `nginx` на сервер.

### Стандартный репозиторий

Пакет `nginx` доступен в репозитории пакетов `apt` в Ubuntu. Однако, в
зависимости от версии Ubuntu - версия пакета `nginx` может быть устарелой.
Если установить на Ubuntu 18.04, то скачается версия от 17 Апреля 2018 г. - `1.14.0`.

```bash
$ apt install nginx
$ nginx -v
nginx version: nginx/1.14.0 (Ubuntu)
```

### Официальный репозиторий

Поэтому, чтобы иметь актуальную версию `nginx`, нужно скачивать пакет из
официального репозитория.

Создать файл `/etc/apt/sources.list.d/nginx.list`, который содержит:

```
deb http://nginx.org/packages/mainline/OS/ CODENAME nginx
deb-src http://nginx.org/packages/mainline/OS/ CODENAME nginx
```

Измените файл, заменив `OS` в конце URL-адреса на `ubuntu` или `debian`, в зависимости
от вашей операционной системы.

Замените `CODENAME` на кодовое имя вашего дистрибутива;

- `jessie` или `stretch` для Debian,
- `trusty`, `xenial`, `artful`, или `bionic` для Ubuntu.

Чтобы узнать `CODENAME`.

```bash
cat /etc/os-release
```

Затем, запустите следующие команды:

```bash
apt update
apt install -y gnupg2
curl -sLO http://nginx.org/keys/nginx_signing.key
apt-key add nginx_signing.key
apt update
apt install -y nginx
```

Проверим версию `nginx`.

```bash
$ nginx -v
nginx version: nginx/1.21.6
```

Версия `1.21.6` выпущена 25 января 2022 года. Она является на момент написания
урока актуальной.

> ⭐️ Задания в данном модуле необходимо выполнять с помощью актуальной версии nginx.

### Полезное

- [инструкция c официального сайта nginx](https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/#installing-a-prebuilt-debian-package-from-the-official-nginx-repository)

### Задание

1. Установить на удаленном сервере stepik наиболее актуальную версию `nginx`.

Для проверки выполните запрос на `127.0.0.1`

```bash
curl http://127.0.0.1
```

Должен прийти такой ответ.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Welcome to nginx!</title>
    <style>
      body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
      }
    </style>
  </head>
  <body>
    <h1>Welcome to nginx!</h1>
    <p>
      If you see this page, the nginx web server is successfully installed and
      working. Further configuration is required.
    </p>

    <p>
      For online documentation and support please refer to
      <a href="http://nginx.org/">nginx.org</a>.<br />
      Commercial support is available at
      <a href="http://nginx.com/">nginx.com</a>.
    </p>

    <p><em>Thank you for using nginx.</em></p>
  </body>
</html>
```

---

### Ответ

root@ds-HP-ProBook-450-15-6-inch-G9-Notebook-PC:/opt/github/fork_TechOrda/nginx/nginx-install# apt install nginx
Чтение списков пакетов… Готово
Построение дерева зависимостей… Готово
Чтение информации о состоянии… Готово         
Следующий пакет устанавливался автоматически и больше не требуется:
  mailcap
Для его удаления используйте «apt autoremove».
Будут установлены следующие дополнительные пакеты:
  nginx-common
Предлагаемые пакеты:
  fcgiwrap nginx-doc
Следующие НОВЫЕ пакеты будут установлены:
  nginx nginx-common
Обновлено 0 пакетов, установлено 2 новых пакетов, для удаления отмечено 0 пакетов, и 2 пакетов не обновлено.
Необходимо скачать 552 kB архивов.
После данной операции объём занятого дискового пространства возрастёт на 1 596 kB.
Хотите продолжить? [Д/н] y
Пол:1 http://kz.archive.ubuntu.com/ubuntu noble-updates/main amd64 nginx-common all 1.24.0-2ubuntu7.1 [31,2 kB]
Пол:2 http://kz.archive.ubuntu.com/ubuntu noble-updates/main amd64 nginx amd64 1.24.0-2ubuntu7.1 [521 kB]
Получено 552 kB за 17с (31,6 kB/s)
Предварительная настройка пакетов …
Выбор ранее не выбранного пакета nginx-common.
(Чтение базы данных … на данный момент установлен 214731 файл и каталог.)
Подготовка к распаковке …/nginx-common_1.24.0-2ubuntu7.1_all.deb …
Распаковывается nginx-common (1.24.0-2ubuntu7.1) …
Выбор ранее не выбранного пакета nginx.
Подготовка к распаковке …/nginx_1.24.0-2ubuntu7.1_amd64.deb …
Распаковывается nginx (1.24.0-2ubuntu7.1) …
Настраивается пакет nginx (1.24.0-2ubuntu7.1) …
Настраивается пакет nginx-common (1.24.0-2ubuntu7.1) …
Created symlink /etc/systemd/system/multi-user.target.wants/nginx.service → /usr/lib/systemd/system/nginx.service.
Обрабатываются триггеры для ufw (0.36.2-6) …
Обрабатываются триггеры для man-db (2.12.0-4build2) …
root@ds-HP-ProBook-450-15-6-inch-G9-Notebook-PC:/opt/github/fork_TechOrda/nginx/nginx-install# nginx -v
nginx version: nginx/1.24.0 (Ubuntu)
