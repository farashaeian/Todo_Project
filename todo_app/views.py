from rest_framework import generics
from .models import Task
from .serializers import CreateTaskSerializer, ListTaskSerializer, ChangeTaskSerializer
from django_filters import rest_framework as filters
from .permissions import ChangePermission

class CreateTask(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = CreateTaskSerializer


class FilterTask(filters.FilterSet):
    deadline = filters.DateTimeFilter(field_name='deadline_date', lookup_expr='exact')
    deadline_lt = filters.DateTimeFilter(field_name='deadline_date', lookup_expr='lt')
    deadline_gt = filters.DateTimeFilter(field_name='deadline_date', lookup_expr='gt')

    class Meta:
        model = Task
        fields = {
            'done': ['exact'],
        }


class ListTask(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = ListTaskSerializer
    filterset_class = FilterTask


class ChangeTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = ChangeTaskSerializer
    permission_classes = [ChangePermission]

