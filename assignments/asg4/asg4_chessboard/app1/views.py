from django.http import HttpResponse
from django.shortcuts import render
import html
def home(request):
    page_data = {
    "rows": [
    {"a8": html.unescape('&#9814;'), "b8": html.unescape('&#9816;'), "c8": html.unescape('&#9815;'), "d8": html.unescape('&#9813;'), "e8": html.unescape('&#9812;'), "f8": html.unescape('&#9815;'), "g8": html.unescape('&#9816;'), "h8": html.unescape('&#9814;')},
    {"a7": html.unescape('&#9817;'), "b7": html.unescape('&#9817;'), "c7": html.unescape('&#9817;'), "d7": html.unescape('&#9817;'), "e7": html.unescape('&#9817;'), "f7": html.unescape('&#9817;'), "g7": html.unescape('&#9817;'), "h7": html.unescape('&#9817;')},
    {"a6": html.unescape('&nbsp;'), "b6": html.unescape('&nbsp;'), "c6": html.unescape('&nbsp;'), "d6": html.unescape('&nbsp;'), "e6": html.unescape('&nbsp;'), "f6": html.unescape('&nbsp;'), "g6": html.unescape('&nbsp;'), "h6": html.unescape('&nbsp;')},
    {"a5": html.unescape('&nbsp;'), "b5": html.unescape('&nbsp;'), "c5": html.unescape('&nbsp;'), "d5": html.unescape('&nbsp;'), "e5": html.unescape('&nbsp;'), "f5": html.unescape('&nbsp;'), "g5": html.unescape('&nbsp;'), "h5": html.unescape('&nbsp;')},
    {"a4": html.unescape('&nbsp;'), "b4": html.unescape('&nbsp;'), "c4": html.unescape('&nbsp;'), "d4": html.unescape('&nbsp;'), "e4": html.unescape('&nbsp;'), "f4": html.unescape('&nbsp;'), "g4": html.unescape('&nbsp;'), "h4": html.unescape('&nbsp;')},
    {"a3": html.unescape('&nbsp;'), "b3": html.unescape('&nbsp;'), "c3": html.unescape('&nbsp;'), "d3": html.unescape('&nbsp;'), "e3": html.unescape('&nbsp;'), "f3": html.unescape('&nbsp;'), "g3": html.unescape('&nbsp;'), "h3": html.unescape('&nbsp;')},
    {"a2": html.unescape('&#9823;'), "b2": html.unescape('&#9823;'), "c2": html.unescape('&#9823;'), "d2": html.unescape('&#9823;'), "e2": html.unescape('&#9823;'), "f2": html.unescape('&#9823;'), "g2": html.unescape('&#9823;'), "h2": html.unescape('&#9823;')},
    {"a1": html.unescape('&#9820;'), "b1": html.unescape('&#9822;'), "c1": html.unescape('&#9821;'), "d1": html.unescape('&#9819;'), "e1": html.unescape('&#9818;'), "f1": html.unescape('&#9821;'), "g1": html.unescape('&#9822;'), "h1": html.unescape('&#9820;')},
    ]
    }
    return render(request, 'app1/home.html', page_data);

def history(request):
    return render(request, 'app1/history.html');

def about(request):
    return render(request, 'app1/about.html');

def rules(request):
    return render(request, 'app1/rules.html');
