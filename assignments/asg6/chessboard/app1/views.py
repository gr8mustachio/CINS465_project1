from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from app1.models import Board
import html
from app1.forms import ChessForm, JoinForm, LoginForm

valid_cols = ["a", "b", "c", "d", "e", "f", "g", "h"]
valid_rows = [1, 2, 3, 4, 5, 6, 7, 8]

@login_required(login_url='/login/')
def home(request):
    page_data = { "rows": [], "chess_form": ChessForm }
    if (Board.objects.filter(user=request.user).count() == 0) or (request.method == 'POST' and 'new_game' in request.POST):
        newGame(request)
    elif (request.method == 'POST'):
        chess_form = ChessForm(request.POST)
        if (chess_form.is_valid()):
            location = chess_form.cleaned_data["location"]
            new_location = chess_form.cleaned_data["new_location"]
            piece = Board.objects.get(user=request.user, name=location).value
            Board.objects.filter(user=request.user, name=location).delete();
            Board(user=request.user, name=new_location, value=piece).save()
            Board(user=request.user, name=location, value = html.unescape('&nbsp;')).save()
        else:
            page_data["chess_form"] = chess_form

        #populate page_data from board model
        #doesn't work with reversed
    for row in reversed(valid_rows):
        row_data = {}
        for col in valid_cols:
            id = "{}{}".format(col,row)
            try:
                record = Board.objects.get(user=request.user, name=id)
                row_data[id] = record.value
            except Board.DoesNotExist:
                row_data[id] = html.unescape('&nbsp;')
        page_data.get("rows").append(row_data)

    return render(request, 'app1/home.html', page_data)




def newGame(request):
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

   #deleting all board model objects
    Board.objects.filter(user=request.user).delete()
    #return render(request, 'app1/home.html', page_data);

    #populating all board model objects from page_data
    for row in page_data.get("rows"):
        for name, value in row.items():
            Board(user=request.user, name=name, value=value).save()

def join(request):
    if(request.method == 'POST'):
        join_form = JoinForm(request.POST)
        if(join_form.is_valid()):
            #save the data to DB
            user = join_form.save()
            #encrypt Password
            user.set_password(user.password)
            #save encrypted password to db
            user.save()
            #success, back to homepage
            return redirect("/")
        else:
            #form is invalid, print error to console
            page_data = { "join_form": join_form }
            return render(request, 'app1/join.html', page_data)
    else:
        join_form = JoinForm()
        page_data = { "join_form": join_form }
        return render(request, 'app1/join.html', page_data)

def user_login(request):
    if(request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if(login_form.is_valid()):
            #get username and password given
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            #django auth function
            user = authenticate(username=username, password=password)
            #if user exists
            if user:
                #check if is_active
                if(user.is_active):
                    #log them in
                    login(request,user)
                    #send to homepage
                    return redirect("/")
                else:
                    #account not active
                    return HttpResponse("Your account is not active.")
            else:
                print("someone tried to login and failed")
                print("they used username: {} and password {}".format(username,password))
                return render(request, 'app1/login.html', {"login_form": LoginForm})
    else:
                #nothing provided
        return render(request, 'app1/login.html', {'login_form': LoginForm})


@login_required(login_url='/login/')
def user_logout(request):
    #log out user
    logout(request)
    #return to homepage
    return redirect("/")

def history(request):
    return render(request, 'app1/history.html');

def about(request):
    return render(request, 'app1/about.html');

def rules(request):
    return render(request, 'app1/rules.html');
