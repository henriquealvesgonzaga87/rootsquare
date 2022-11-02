from multiprocessing import context
from django.shortcuts import render
from .forms import Form
from math import sqrt

# Create your views here.

def index(request):
    
    if request.method == 'POST':
        form = Form(request.POST)

        if form.is_valid():
            a = float(form.data['a'])
            b = float(form.data['b'])
            c = float(form.data['c'])
            
            r = list() #to follow the  jinja's variable on index 
            if b*b - 4*a*c > 0:
                r.append((-b + sqrt(b*b - 4*a*c)) / 2*a)
                r.append((-b - sqrt(b*b - 4*a*c)) / 2*a)
                context = {'form': Form, 'r': r}
            elif b*b - 4*a*c == 0:
                r.append(-b / 2*a)
                context = {'form': Form, 'r': r}
            else:
                context = {'form': Form, 'sr': True}

            return render(request, 'index.html', context=context)
    else:
        context = {'form': Form}
        return render(request, 'index.html', context=context)
