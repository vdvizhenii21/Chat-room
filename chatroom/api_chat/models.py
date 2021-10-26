from django.db import models


class Message(models.Model):
    author = models.CharField(db_index=True, max_length=30,)
    email = models.EmailField(('email address'), blank=False, unique=True)
    text = models.TextField(
        "Текст",
        help_text="Напишите текст"
    )
    create_date = models.DateTimeField("date published", auto_now_add=True)
    upd_date = models.DateTimeField(auto_now=True)
