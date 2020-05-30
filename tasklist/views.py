from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.
def index(request):
    tasklist = TaskList.objects.all()
    form = TaskListForm()

    if request.method == 'POST':
        form = TaskListForm(request.POST)
        if form.is_valid():
            messages.success(request, "Title saved successfully")
            form.save()
        else:
            messages.error(request, "Please ensure Title has at most 250 characters.")
            # return HttpResponse("Please enter title with less than 250 characters.. ")

        return redirect('/')
    context = {'tasklist': tasklist, 'form':form}
    return render(request, 'tasklist/list.html', context)


def updateTask(request, pk):
    task = TaskList.objects.get(id=pk)

    form = TaskListForm(instance=task)

    if request.method == 'POST':
        form = TaskListForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Title updated successfully")
            return redirect('/')
        else:
            messages.error(request, "Please ensure Title has at most 250 characters.")

    context = {'form': form}
    return render(request, 'tasklist/update_task.html', context)


def deleteTask(request, id):
    item = TaskList.objects.get(id=id)

    if request.method =='POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'tasklist/delete_task.html', context)