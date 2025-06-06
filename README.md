<h1 align="center" id="title">МКПедия</h1>

<p align="center"><img src="https://socialify.git.ci/MKfun/mkpedia/image?language=1&amp;owner=1&amp;name=1&amp;stargazers=1&amp;theme=Light" alt="project-image"></p>

<p id="description">Вики-движок написанный Беном Сралденом не без помощи великих Денчика (css) и спбога (хостит проект).</p>

<h2>📷 Скриншоты:</h2>

<img src="https://github.com/TimurSennikov/mkpedia_screenshots/blob/main/main_page_0.png?raw=true" alt="project-screenshot" width="100%" height="100%/">

<img src="https://github.com/TimurSennikov/mkpedia_screenshots/blob/main/login_page_0.png?raw=true" alt="project-screenshot" width="100%" height="100%/">

  
  
<h2>🧐 Фичи</h2>

Некоторые из фич проекта:

*   Публикация статей
*   Редактирование Статей
*   История коммитов статей
*   Легковесность
*   Отличный CSS (спасибо @den4iklovelinux!)
*   Почтовый ящик

<h2>🛠️ Установка:</h2>

<p>1. Клонируйте репозиторий и перейдите в директорию mkpedia.</p>

```
git clone https://github.com/MKfun/mkpedia.git
```

<p>2. Запустите setup.sh</p>

```
bash setup.sh
```

  
  
<h2>💻 Сделано на</h2>

Инструменты, использовавшиеся для создания проекта:
*   Python
*   Flask
*   Jinja2

<h2>🐧 Переход с 0.8 на 0.9+</h2>
На версии 0.9 поменялась структура БД, перед выполнением следующих действий рекомендуется сделать бекап instance.
Раскомментируйте в mk/app.py строки 57, 58 и 59, запустите сервер через файл migrate.sh (это важно) и перейдите на /migrate. Выключите сервер и удалите (забекапив) instance/mkpedik.db, закомментируйте ранее раскомментированные строки (а лучше вообще удалите их) и запустите сервер.
<h3>root при переносе не копируется, у него будет дефолтный пароль toor!!!</h3>

<h2>🛡️ Лицензия</h2>
Проект использует лицензию zlib
