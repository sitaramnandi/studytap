from rest_framework import serializers
from api.models import student
class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields=["id","stname","age"]