from rest_framework import serializers
from .models import Bmi


class BmiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bmi
        fields = ('id', 'weight', 'height', 'bmi', 'date')
