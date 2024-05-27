
from django.http import HttpResponse
from django.shortcuts import redirect, render
from todoapp.models import Task
from .forms import TodoForm
from django .views .generic import ListView
from django .views .generic.detail import DetailView
from django .views .generic import UpdateView
from django .views .generic import DeleteView
# Create your views here.

class Tasklistview(ListView):
    model=Task
    template_name="home.html"
    context_object_name="task1"

class Taskdetailview(DetailView):
    model=Task
    template_name="details.html"
    context_object_name="task"


class Taskupdateview(UpdateView):
    model=Task                  
    template_name='update.html'
    context_object_name='task'
    fields=['field1','priority','date']
    success_url='/' 
    
class Taskdeleteview(DeleteView):
    model=Task
    template_name="delete.html"
    success_url='/'

def add(request):
    task2=Task.objects.all()
    if request.method=="POST":
        name=request.POST.get("task",'')
        priority=request.POST.get("priority",'')
        date=request.POST.get("date","")
        task1=Task(field1=name,priority=priority,date=date)
        task1.save()

    return render(request,"home.html",{"task1":task2})

# def details(request):
    
#     return render(request,"details.html",})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=="POST":
        task.delete()
        return redirect("/")        
    return render(request,"delete.html")
    

def update(request,id):

    task=Task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect("/")
    return render(request,"edit.html",{"f":f,"task":task})
