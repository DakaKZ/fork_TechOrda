# nginx-ufw

На вашем сервере может быть запущено несколько сервисов помимо nginx. Оставлять доступ к ним открытым из Интернета может быть очень опасно.
Злоумышленники могут этим воспользоваться и взломать один из открытых сервисов.

Для безопасности, нужно закрыть к ним доступы и оставить только доступ к веб-серверу nginx. Одним из способов это сделать является команда `ufw`.

На данном уроке, мы научимся как обезопасить свой сервер.

### Полезные ссылки

- [UFW - Uncomplicated Firewall](https://help.ubuntu.com/community/UFW)
- [Hello Linux: Nginx & UFW Firewall](https://www.codingforentrepreneurs.com/blog/hello-linux-nginx-and-ufw-firewall)

### Задание

1. На своем компьютере запустите nginx. Скачайте `ufw` и настройте доступ извне только на порты 80 и 443.
2. Отправьте выполненные команды.

---

### Ответ
root@ds-HP-ProBook-450-15-6-inch-G9-Notebook-PC:/opt/github/fork_TechOrda/nginx/nginx-cert# ufw allow 80/tcp
Правила обновлены
Правила обновлены (v6)
root@ds-HP-ProBook-450-15-6-inch-G9-Notebook-PC:/opt/github/fork_TechOrda/nginx/nginx-cert# ufw allow 443/tcp
Правила обновлены
Правила обновлены (v6)
root@ds-HP-ProBook-450-15-6-inch-G9-Notebook-PC:/opt/github/fork_TechOrda/nginx/nginx-cert# sudo ufw enable
Межсетевой экран включён и будет запускаться при запуске системы
root@ds-HP-ProBook-450-15-6-inch-G9-Notebook-PC:/opt/github/fork_TechOrda/nginx/nginx-cert# sudo ufw status
Состояние: активен

В                          Действие    Из
-                          --------    --
8080/tcp                   ALLOW       Anywhere                  
80/tcp                     ALLOW       Anywhere                  
443/tcp                    ALLOW       Anywhere                  
8080/tcp (v6)              ALLOW       Anywhere (v6)             
80/tcp (v6)                ALLOW       Anywhere (v6)             
443/tcp (v6)               ALLOW       Anywhere (v6)
