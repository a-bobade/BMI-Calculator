from rest_framework import viewsets
from .models import Bmi
from .serializers import BmiSerializer


class BmiViewSet(viewsets.ModelViewSet):
    queryset = Bmi.objects.all()
    serializer_class = BmiSerializer

