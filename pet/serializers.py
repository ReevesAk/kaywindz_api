from rest_framework import serializers
from .models import PetInfo, Sex

# Serializers define the API representation.
class PetInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PetInfo
        fields = ['id', 'pet_name', 'image', 'breed', 'description', 'color','country_of_origin',
         'age_in_months', 'sex', 'quantity']


class SexSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sex
        fields = ['id','gender']