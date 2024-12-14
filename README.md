# Тестовое задание Betting Software

Стек: `Python`, `FastAPI`, `SQLAlchemy`, `PostgreSQL`, `REST API`, `Docker Compose`, `Nginx`

Разработать систему, принимающую пользовательские ставки на определённые события (например, спортивные).

Система должна состоять из двух независимых сервисов:

- сервис **line-provider** - провайдер информации о событиях;
- сервис **bet-maker** - принимающий ставки на эти события от пользователя.

## Описание сервиса line-provider

Сервис должен выдавать информацию о событиях, на которые можно совершать ставки.
Система будет упрощённой, поэтому будет принимать ставки только на выигрыш первой команды.

Информация о событии должна содержать как минимум:

- уникальный идентификатор события — строка или число,
- коэффициент ставки на выигрыш — строго положительное число с двумя знаками после запятой,
- дедлайн для ставок — таймстемп, до которого на событие принимаются ставки,
- текущий статус события.

В системе событие может иметь один из трёх статусов:

- незавершённое,
- завершено выигрышем первой команды,
- завершено выигрышем второй команды и, соответственно, поражением первой (ничьих в наших событиях не бывает).

**API** сервиса **line-provider** не регламентировано и остаётся на ваше усмотрение.
Информация о событиях может храниться в памяти, без использования каких-либо
сторонних хранилищ.

## Описание сервиса bet-maker

Сервис отвечает за постановку ставок на события пользователями.

Информация о событиях должна получаться из сервиса **line-provider**. В частности, сервису **bet-maker** необходимо узнавать об изменении статуса событий (переход в статус завершено с выигрышем или поражением), чтобы понять выиграла ставка или проиграла.

Взаимодействие между сервисами может быть реализовано, к примеру, запросами в сервис **line-provider**, вызовом callback-урла **bet-maker** при изменении статуса события на стороне **line-provider** или обменом сообщений между сервисами через очередь.

## Требования

Рекомендованный фреймворк для реализации сервисов — **FastAPI**, версия **Python** — 3.10.

Взаимодействия между сервисами **line-provider** и **bet-maker**, а также между сервисами и их хранилищами должны быть полностью асинхронными.

Сервисы **line-provider** и **bet-maker**, а также дополнительные хранилища и прочие инфраструктурные элементы должны быть докеризированы и запускаться через **docker compose**.

## Первичная настройка

```bash
~ git clone https://github.com/anton-savenchuk/BSW-Test
~ cd bsw-test
```

Необходимо изменить файл `.env.example`, указав свои переменные окружения, и переименовать его в `.env`

## Сборка и запуск docker-compose

```bash
~ cd bsw-test
~ docker compose up --build
```

## После сборки проекта сервисы доступны:

### line-provider

- API: [http://localhost/line-provider/](http://localhost/line-provider/)
- Swagger (документация): [http://localhost/line-provider/docs/](http://localhost/line-provider/docs/)

### bet-maker

- API: [http://localhost/bet-maker/](http://localhost/bet-maker/)
- Swagger (документация): [http://localhost/bet-maker/docs/](http://localhost/bet-maker/docs/)
