from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, "Pizzas/index.html")

def pizzas(request):
    pizzas = Pizza.objects.order_by('pizza_name')

    context = {'allpizzas': pizzas}
    return render(request, 'Pizzas/pizzas.html', context)

def pizza(request,pizza_id):
    p = Pizza.objects.get(id=pizza_id)
    toppings = Topping.objects.filter(pizza=p)
    addcomment = Comment.objects.filter(pizza=pizza_id)
    image = Image.objects.filter(pizza=pizza_id)

    context = {'pizza':p, 'toppings':toppings, 'addcomment':addcomment, 'image':image}
    return render(request, 'Pizzas/pizza.html', context)
    '''
    p= Pizza.objects.get(id=pizza_id)
    toppings = Topping.objects.filter(pizza_name=pizza_name)
    addcomment = Comment.objects.filter(pizza_name=pizza_name)
    image = Image.objects.filter(pizza_name=pizza_name_id)

    context = {'pizza_name':pizza_name, 'toppings':toppings, 'addcomment':addcomment, 'image':image}
    return render(request, 'Pizzas/pizza.html', context)
'''
def comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.pizza = pizza
            comment.save()
            return redirect('Pizzas:pizza',pizza_id=pizza_id)

    context = {'form':form,'pizza':pizza}
    return render(request, 'Pizzas/comment.html', context)