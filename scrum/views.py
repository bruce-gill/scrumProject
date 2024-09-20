from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializer import *
from rest_framework import permissions, viewsets

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = project.objects.all()
    serializer_class = projectSerializer
    permission_classes = [permissions.IsAuthenticated]



