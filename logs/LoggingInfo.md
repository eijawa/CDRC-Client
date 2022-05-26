# Информация по текущему логированию

Сейчас логи записываются и хранятся в течение 3-х дней. Длительность хранения можно изменить.

## Описание полей обработчика

> [Документация](https://docs.python.org/3/library/logging.config.html#module-logging.config "Официальная документация по модульным логам")

```json
"file": {
  "class": "logging.handlers.TimedRotatingFileHandler",
  "formatter": "clientFormatter",
  "filename": "logs/client.log",
  "backupCount": 3,
  "utc": true,
  "when": "D",
  "interval": 3,
  "encoding": "UTF-8"
}
```

`class` - Базовый класс, используемый для обработки. [`TimedRotatingFileHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.TimedRotatingFileHandler "Официальная документация по интервальному логированию") записывает сообщения в файлы, которые обновляются с некоторым интервалом.<br/>
`backupCount` - максимальное количество файлов логирования. Значение должно совпадать с `interval`, чтобы не оставлять после себя лишних файлов.<br/>
`when` - значение для счёта. В данном случае 'D' - дни.<br/>
`interval` - значение интервала для счёта.<br/>

## `clientLogger`

Данный логгер не используется, поскольку пока в нём нет необходимости. Он может понадобиться в будущем, когда возникнет необходимость в отправке логов на сторонний сервер, например, для отображения в веб-интерфейсе.

```json
"loggers": {
  "clientLogger": {
    "level": "DEBUG",
    "handlers": ["file"],
    "propagate": false
  }
},
```

Вместо этого, все текущие параметры и настройки логирования используются сразу же корнем (`root`).
