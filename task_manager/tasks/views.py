from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.core.exceptions import ValidationError
from django.utils.dateparse import parse_datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redireciona o usuário para a página de login após o registro
    else:
        form = UserCreationForm()
    
    return render(request, 'tasks/register.html', {'form': form})


def home(request):
    return render(request, 'tasks/home.html')  # Renderiza o template home.html

@login_required
# Listar todas as tarefas
def task_list(request):
    tasks = Task.objects.filter(user=request.user)  # Filtra as tarefas pelo usuário logado
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
# Crair uma noa tarefa
def task_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        due_date = request.POST.get('due_date', None)
        Task.objects.create(title=title, description=description, due_date=due_date, user=request.user)
        return redirect('task_list')
    return render(request, 'tasks/task_form.html')


# Atualizar uma tarefa existente
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST.get('description', '')
        
        due_date = request.POST.get('due_date', None)
        
        if due_date:
            # Tentar converter a string recebida em um objeto datetime
            parsed_due_date = parse_datetime(due_date)
            if parsed_due_date is None:
                raise ValidationError("Formato de data/hora inválido.")
            task.due_date = parsed_due_date
        
        task.save()
        return redirect('task_list')
    
    return render(request, 'tasks/task_form.html', {'task': task})


# Deletar ua tarefa
def task_delete(request,pk):
    task = get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request,'tasks/task_confirm_delete.html',{'task':task})