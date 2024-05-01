from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def get_default_user():
    return None


class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user, related_name="todolist",
                             null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    todoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text