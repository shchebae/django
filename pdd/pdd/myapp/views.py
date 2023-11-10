from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.generic import DeleteView, UpdateView


def index(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'myapp/index.html', {'tasks': tasks})

def forms(request):
    error = ""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {'form': form, 'error': error}
    return render(request, 'myapp/form.html', context)

class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/'
    template_name = 'myapp/task-delete.html'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'myapp/form.html'
    form_class=TaskForm
    success_url = '/'
