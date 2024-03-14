from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
people = []


class Person:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __str__(self):
        return self.name

class NewPersonForm(forms.Form):
    name = forms.CharField(label="name")
    password = forms.CharField(label="password")

def homePage(request):
    return render(request,"links/homePage.html", {
        'people': people
    })


def add(request):
    if request.method == "POST":
        form = NewPersonForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            password = form.cleaned_data["password"]

            newperson = Person(name, password) 
            people.append(newperson)
            return HttpResponseRedirect(reverse("myapp:homepage"))
    else:
        form = NewPersonForm()
        return render(request,"links/add.html", {'form': form, 'people':people})
    
    
    