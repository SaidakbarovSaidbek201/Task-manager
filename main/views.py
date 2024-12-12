from django.shortcuts import render
from django.http import HttpResponse
from .models import Books

# Create your views here.
def say_hello(requests):
    books = Books.objects.all()
    context = {
        "books": books
    }
    return render(requests, template_name="index.html", context=context)