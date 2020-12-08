from rest_framework import status, viewsets

from .models import TaskModel
from .serializer import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
