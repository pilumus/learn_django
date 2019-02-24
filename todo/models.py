from django.db import models


#создает класс TodoItem, parent = Model с содержимым в виде текста.
class TodoItem(models.Model):
    content = models.TextField()
