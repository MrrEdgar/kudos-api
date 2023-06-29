from rest_framework import serializers
from .models import User, Kudos

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        depth=1
        fields = '__all__'

class KudosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kudos
        fields = '__all__'