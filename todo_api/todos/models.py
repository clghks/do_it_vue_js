from django.db import models


# Create your models here.
class Todo(models.Model):
    todo = models.CharField(max_length=1000)
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.todo
