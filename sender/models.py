from django.db import models

NULLABLE = {
    "blank": True,
    "null": True
}


class Client(models.Model):
    email = models.EmailField(verbose_name='email')
    first_name = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    comment = models.TextField(**NULLABLE, verbose_name='комментарий')

    class Meta:
        verbose_name = 'получатель'
        verbose_name_plural = 'получатели'

    def __str__(self):
        return f"Клиент: {self.last_name} {self.first_name}, почта {self.email}"


class Message(models.Model):
    title = models.CharField(max_length=150, verbose_name='тема письма')
    body = models.TextField(verbose_name='тело письма')

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'

    def __str__(self):
        return self.title


class Newsletter(models.Model):
    STATUS_CHOICES = (
        ('created', 'создана'),
        ('launched', 'запущена'),
        ('completed', 'завершена'),
    )
    first_sending = models.DateTimeField(verbose_name='первая отправка')
    last_sending = models.DateTimeField(**NULLABLE, verbose_name='последняя отправка')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, verbose_name='статус')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение')
    clients = models.ManyToManyField(Client, verbose_name='получатели')

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'

    def __str__(self):
        return f"{self.first_sending} {self.status}"
