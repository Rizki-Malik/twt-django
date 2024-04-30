from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewListForm

# Create your views here.


def index(response):
    return render(response, "task/home.html", {})


def detail(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "task/list.html", {"ls": ls})


def create(response):
    if response.method == "POST":
        form = CreateNewListForm(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewListForm()

    return render(response, "task/create.html", {"form": form})




