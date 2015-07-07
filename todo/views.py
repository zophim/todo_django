from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST, require_http_methods
from .models import Todo

# Create your views here.
def index(request):
    todos = []
    authenticated = request.user.is_authenticated()
    if authenticated:
        todos = Todo.objects.filter(user=request.user)
    context = { 
        'todos': todos,
        'username': request.user.username if request.user.username != '' else 'New User',
        'authenticated': authenticated
    }
    return render(request, 'todo/index.html', context)

@require_POST
def create(request):
    if not request.user.is_authenticated():
        return HttpResponseBadRequest("Must be signed in to create a Todo item.")
    name = request.POST.get('name')
    if not name:
        return HttpResponseBadRequest("Must provide a name.")
    latest_order = 0
    if Todo.objects.count() > 0:
        latest_order = Todo.objects.order_by('-order')[:1].get().order
    todo = Todo.objects.create(name=name, order=latest_order + 1, user=request.user)
    return redirect('todo.views.index')

@require_http_methods(['DELETE'])
def remove(request, id):
    if not request.user.is_authenticated():
        return HttpResponseBadRequest("Must be signed in to remove a Todo item.")
    todo = get_object_or_404(Todo, pk=id)
    if request.user != todo.user:
        return HttpResponseBadRequest("Must own the Todo item to remove it.")
    todo.delete()
    return HttpResponse("Okay")

