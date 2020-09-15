from django.shortcuts import render
from api.models import Task
# Create your views here.
def TaskList(request):
    task = Task.objects.all()

    context = {
        'task':task,
    }
    return render(request,'home/index.html')