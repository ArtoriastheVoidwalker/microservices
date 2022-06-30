# README

This README would normally document whatever steps are necessary to get your application up and running.

### Инструкция для сборки и запуска приложения на локальном компьютере:

1. Склонировать проект
2. Добавить файл event.conf в директорию `/etc/nginx/conf.d/`
3. Добавить в файл `/etc/hosts` строки `127.0.0.1   line-provider.local` и `127.0.0.1   bet.local`
4. Перейти в репозиторий backend
5. Запустить *`./docker_prepare.sh`*
6. Для запуска backend перейти в корень папки и запустить `./dev.sh`
7. Перейти в репозиторий line-provider и повторить действия пунктов 3 и 4
