from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import main
import pandas as pd


@login_required
def taskList(request):

    search = request.GET.get('search')

    if search:
        tasks = Task.objects.filter(name__icontains=search)
    else:
        tasks_list = Task.objects.all().order_by('-type_task')
        paginator = Paginator(tasks_list, 12) #quantidde de linhas
        page = request.GET.get('page')
        tasks = paginator.get_page(page)

    return render(request, 'conta/list.html', {'tasks': tasks})

@login_required
def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'conta/task.html', {'task': task})


@login_required
def newTask(request):

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'A_Pagar'
            task.save()

            return redirect('/')

    else:
        form = TaskForm()
        return render(request, 'conta/addtask.html', {'form': form})

@login_required
def editTask(request, id):
    #task = Task.objects.create(description ="GfG is the best")
    #task.save()

    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            task.save()
            return redirect('/')
        else:
            return render(request, 'conta/edittask.html', {'form': form, 'task': task})

    else:
        return render(request, 'conta/edittask.html', {'form': form, 'task': task})



@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso.')
    return redirect('/')


@login_required
def faturaTask(request):
    df = main.read_sql()
    df2 = main.read_sql2()
    x = df.varcont
    y = df2.varcont

    new = []
    for a in x:
        new.append(a)

    dd = pd.DataFrame(data=new,columns=['Calc'])
    faturar_x = dd['Calc'].sum()

    new2 = []
    for a in y:
        new2.append(a)

    dd = pd.DataFrame(data=new2,columns=['Calc'])
    faturar_y = round(float(dd['Calc'].sum()),2)

    faturamento = faturar_y + faturar_x


    return render(request, 'conta/fatura.html', {'faturar_x': faturar_x,'faturar_y': faturar_y,'faturamento': faturamento})








#Testes
def yourName(request):
    nome = 'ok'
    return render(request, 'conta/list.html', {'nome': nome})


def helloworld(request):
    return HttpResponse('Hello World!')




