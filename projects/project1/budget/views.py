from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from budget.models import BudgetItem, BudgetCategory
from budget.forms import BudgetForm #TaskCategoryForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import html

# Create your views here.
@login_required(login_url='/login/')
def main(request):
    if(BudgetCategory.objects.count() == 0):
        BudgetCategory(category = 'Food').save()
        BudgetCategory(category = 'Clothing').save()
        BudgetCategory(category = 'Housing').save()
        BudgetCategory(category = 'Education').save()
        BudgetCategory(category = 'Entertainment').save()
    if(request.method == "GET" and 'delete' in request.GET):
        id=request.GET['delete']
        BudgetItem.objects.filter(id=id).delete()
        return redirect('/main_budget/')
    else:
        table_data = BudgetItem.objects.filter(user=request.user)
        surpOrDef = 0
        for row in table_data:
            leftOver = row.projected - row.actual
            surpOrDef+=leftOver
        if(surpOrDef < 0):
            deficit = True
            surpOrDef*=-1
        else:
            deficit = False
        context = {
            'table_data' : table_data,
            'surpOrDef' : surpOrDef,
            'deficit' : deficit
        }

        return render(request, 'budget/budget.html', context)


@login_required(login_url='/login/')
def add(request):
    print("add!")
    if(request.method == "POST"):
        add_form = BudgetForm(request.POST)
        if(add_form.is_valid()):
            budgetItem = add_form.save(commit=False)
            budgetItem.user = request.user
            budgetItem.save()
            return redirect('/main_budget/')
        else:
            context = {
                'form-data': add_form
            }
            return render(request, 'budget/add.html', context)
    else:
        context = { 'form_data' : BudgetForm() }
        return render(request, 'budget/add.html', context)



@login_required(login_url='/login/')
def edit(request, id):
    if(request.method == 'GET'):
        #load budget form with current model form
        budgetItem = BudgetItem.objects.get(id=id)
        form = BudgetForm(instance=budgetItem)
        context = { 'form_data' : form }
        return render(request, 'budget/edit.html', context)
    elif(request.method == 'POST'):
        if('edit' in request.POST):
            form = BudgetForm(request.POST)
            if(form.is_valid()):
                #Saving with commit=False gets you a model object,
                #then you can add your extra data and save it.
                budgetItem = form.save(commit=False)
                budgetItem.user = request.user
                budgetItem.id = id
                budgetItem.save()
                return redirect('/main_budget/')
            else:
                context = { 'form_data' : form_data }
                return render(request, 'budget/add.html', context)
        else:
            #clancel
            return redirect('/main_budget/')


    #return HttpResponse("edit page")
