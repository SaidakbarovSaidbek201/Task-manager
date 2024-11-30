from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(requests):
    text = """HELLO MY NAME IS SAIDBEK! HELLO WORLD!
    <br>SALOM MENING ISMIM SAIDBEK! SALOM DUNYO!
    <br>ПРИВЕТ МЕНЯ ЗОВУТ САИДБЕК! ПРИВЕТ МИР!"""
    return HttpResponse(text)