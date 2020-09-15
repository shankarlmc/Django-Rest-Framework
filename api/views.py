from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer
from django.http import JsonResponse
# Create your views here.


@api_view(['GET'])
def task_list(request):
    task1 = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(task1, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def task_detail(request, pk):
    task1 = Task.objects.get(id=pk)
    serializer = TaskSerializer(task1, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def task_update(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response('item deleted successfully')