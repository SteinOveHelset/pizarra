from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from project.models import Project
from todolist.models import Todolist
from .models import Task


@login_required
def add(request, project_id, todolist_id):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=todolist_id)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        Task.objects.create(project=project, todolist=todolist, name=name, description=description, created_by=request.user)

        return redirect(f'/projects/{project_id}/{todolist_id}/')

    return render(request, 'task/add.html')


@login_required
def detail(request, project_id, todolist_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=todolist_id)
    task = Task.objects.filter(project=project).filter(todolist=todolist).get(pk=pk)

    if request.GET.get('is_done', '') == 'yes':
        task.is_done = True
        task.save()

    return render(request, 'task/detail.html', {
        'task': task
    })


@login_required
def edit(request, project_id, todolist_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=todolist_id)
    task = Task.objects.filter(project=project).filter(todolist=todolist).get(pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        if name:
            task.name = name

        task.description = description
        task.save()

        return redirect(f'/projects/{project_id}/{todolist_id}/{pk}/')

    return render(request, 'task/edit.html', {
        'task': task
    })


@login_required
def delete(request, project_id, todolist_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=todolist_id)
    task = Task.objects.filter(project=project).filter(todolist=todolist).get(pk=pk)
    task.delete()

    return redirect(f'/projects/{project_id}/{todolist_id}/')