from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Theme(models.Model):
    text = models.TextField(
        'Текст темы',
        help_text='Введите текст темы'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='themes',
        verbose_name='Автор',
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    theme = models.ForeignKey(
        Theme,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    author = models.ForeignKey(
        User,
        verbose_name=("Автор"),
        on_delete=models.CASCADE,
    )
    text = models.TextField('Текст комментария')
    created = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
