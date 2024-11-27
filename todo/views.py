from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, Tag
from .forms import TaskForm, TagForm

# Відображення домашньої сторінки
def home(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'todo/home.html', {'tasks': tasks})


# Створення завдання
def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'todo/task_form.html', {'form': form})

# Оновлення завдання
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/task_form.html', {'form': form})

# Видалення завдання
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')

# Зміна статусу завдання (Complete/Undo)
def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done  # Перемикаємо статус
    task.save()  # Зберігаємо зміни в базі даних
    return redirect('home')


# Сторінка для списку тегів
def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'todo/tag_list.html', {'tags': tags})

# Створення тегу
def tag_add(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tag_list')
    else:
        form = TagForm()
    return render(request, 'todo/tag_form.html', {'form': form})

# Оновлення тегу
def tag_update(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('tag_list')
    else:
        form = TagForm(instance=tag)
    return render(request, 'todo/tag_form.html', {'form': form})

# Видалення тегу
def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    tag.delete()
    return redirect('tag_list')


def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect('task_list')