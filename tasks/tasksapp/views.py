
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tasks
from .serializers import TaskSerializer
from rest_framework import generics
from django.shortcuts import render, redirect
from .forms import TaskForm

# Create your views here.

class TaskCreateSerializer(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()  # Correct the attribute name to 'queryset'
    serializer_class = TaskSerializer

class TaskRetriveUpdateSerialzer(generics.RetrieveUpdateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'

class TaskListView(APIView):
    def get(self, request):
        tasks = Tasks.objects.all()  # Get all instances of the Task model
        serializer = TaskSerializer(tasks, many=True)  # Serialize the queryset (many=True as it's multiple objects)

        return Response(serializer.data)
    
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-list')  # Redirect to the task list page after successful form submission
    else:
        form = TaskForm()

    return render(request, 'create_task.html', {'form': form})





