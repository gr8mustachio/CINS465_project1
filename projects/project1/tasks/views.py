from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from tasks.models import Task, TaskCategory
from tasks.forms import TaskEntryForm #TaskCategoryForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import html

# Create your views here.
@login_required(login_url='/login/')
def main(request):
    print("hello")
    if(TaskCategory.objects.count() == 0):
        TaskCategory(category = "Home").save()
        TaskCategory(category = "Work").save()
        TaskCategory(category = "School").save()
        TaskCategory(category = "Personal Improvment").save()
        TaskCategory(category = "Relationships").save()
        TaskCategory(category = "Other").save()  
    if(request.method == "GET" and "delete" in request.GET):
        id=request.GET["delete"]
        Task.objects.filter(id=id).delete()
        return redirect("/main_tasks/")
    elif(request.method == "GET" and "no" in request.GET):
        print("no to Yes")
        id=request.GET["no"]
        Task.objects.filter(id=id).is_completed = True
        Task.objects.filter(id=id).save()
        return redirect('/main_tasks/')
    elif(request.method == "GET" and "yes" in request.GET):
            print("yes to no")
            id=request.GET["yes"]
            Task.objects.filter(id=id).is_completed = False
            Task.objects.filter(id=id).save()
            return redirect('/main_tasks/')
    else:
        table_data = Task.objects.filter(user=request.user)
        context = {
            "table_data" : table_data
        }
        return render(request, 'tasks/tasks.html', context)


@login_required(login_url='/login/')
def add(request):
    if(request.method == "POST"):
        if("add" in request.POST):
            add_form = TaskEntryForm(request.POST)
            if (add_form.is_valid()):
                # description = add_form.cleaned_data["description"]
                # category = add_form.cleaned_data["category"]
                # user = User.objects.get(id=request.user.id)
                # is_completed = False
                # Task(user=user, description=description, category=category, is_completed=is_completed).save()
                taskEntry = add_form.save(commit=False)
                taskEntry.user = request.user
                taskEntry.save()
                return redirect("/main_tasks/")
            else:
                context = {
                    "form_data": add_form
                }
                return render(request, 'tasks/add.html', context)
        else:
            #Cancel
            return redirect("/main_tasks/")
    else:
        context = {
            "form_data" : TaskEntryForm()
        }
        return render(request, 'tasks/add.html', context)

    #return HttpResponse("add view")
@login_required(login_url='/login/')
def edit(request, id):
    if (request.method == "GET"):
        #Load task entry form with current model form
        taskEntry = Task.objects.get(id=id)
        form = TaskEntryForm(instance=taskEntry)
        context = { 'form_data': form }
        return render(request, 'tasks/edit.html', context)
    elif (request.method == "POST"):
        if("edit" in request.POST):
            form = TaskEntryForm(request.POST)
            if(form.is_valid()):
                #Saving with commit=False gets you a model object,
                #then you can add your extra data and save it.
                taskEntry = form.save(commit=False)
                taskEntry.user = request.user
                taskEntry.id = id
                taskEntry.save()
                return redirect('/main_tasks/')
            else:
                context = {
                    "form_data" : form
                }
                return render(request, 'tasks/add.html', context)
        else:
            #Cancel
            return redirect("/main_tasks/")
    #return HttpResponse("edit template")
