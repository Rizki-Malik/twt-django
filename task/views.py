from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.


def index(response):
    return render(response, "task/home.html", {})


def detail(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "task/list.html", {"ls": ls})

