from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm, EquacaoForm
import math

def index (Request):
    form = EquacaoForm(Request.POST)
    if form.is_valid():
        a = form.cleaned_data['a']
        b = form.cleaned_data['b']
        c = form.cleaned_data['c']
        result = equacao(a, b, c)
    context = {
        'form' : form,
        'result' : result
    }

    return render(Request, 'user/index.html', context=context)

def create (Request):
    #GET
    #POST
    #PUT -ATUALIZAÇÃO
    #DELETE
    if Request.method == 'GET':
        form = UserForm()
        context = {
            'form': form
        }
        return render(Request, 'user/create.html', context=context)
    else:
        form = UserForm(Request.POST)
        if form.is_valid():
            context = {
                'form': form,
                'nome' : form.cleaned_data['nome'],
                'telefone' : form.cleaned_data['telefone'],
                'email': form.cleaned_data['email'],
            }
        return render(Request, 'user/create.html', context=context)

def modify (Request, user_id):
    context = {
        'id': user_id
    }
    return render(Request, 'user/create.html', context=context)

def equacao(a = 0, b = 0, c = 0):
    if(b != 0 and c != 0) :
        delta = pow(b, 2) - 4 * a * c
        resultPositive = ((-b) + math.pow(delta, 1/2)) / 2 * a
        resultNegative = ((-b) - math.pow(delta, 1/2)) / 2 * a
        return 'As raízes são ' + str(resultPositive) + ' e ' + str(resultNegative) + '.'
    elif(b == 0 and a != 0) :
        ZeroDivisionError
        resultNegative = - (math.pow(c, 1/2) / a)
        resultPositive = + (math.pow(c, 1/2) / a)
        return 'As raízes são ' + str(resultPositive) + ' e ' + str(resultNegative) + '.'
    elif(c == 0 and a != 0) :
        result = - (b) / a
        return 'As raízes são 0 e ' + str(result) + '.'
    else :
        result = 'Não foi possível calcular.'
        return result
   