from urllib import request

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewListForm

# Create your views here.


def index(response):
    return render(response, "task/home.html", {})


def detail(response, id):
    ls = ToDoList.objects.get(id=id)

    if response.method == 'POST':
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False

                item.save()

        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("invalid")

    return render(response, "task/list.html", {"ls": ls})


def create(response):
    if response.method == "POST":
        form = CreateNewListForm(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n, user=response.user)
            t.save()

            return HttpResponseRedirect("/%i" % t.id)
    else:
        if response.user.is_authenticated:
            form = CreateNewListForm()
        else:
            return HttpResponseRedirect("/login/")

    return render(response, "task/create.html", {"form": form})


def view(response):
    return render(response, "task/view.html", {})

