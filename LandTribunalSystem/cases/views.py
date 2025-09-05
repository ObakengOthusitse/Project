from django.shortcuts import render
from rest_framework import viewsets
from .models import Case
from .serializers import CaseSerializer
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

