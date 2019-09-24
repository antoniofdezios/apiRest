from .models import Food
from rest_framework import serializers

class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = ('foodId','name','brand')