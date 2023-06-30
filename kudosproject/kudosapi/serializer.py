from rest_framework import serializers
from datetime import datetime
from .models import User, Kudos

class UserSerializer(serializers.ModelSerializer):
    kudos_left = serializers.SerializerMethodField()

    class Meta:
        model = User
        depth=1
        fields = ('id', 'fullname', 'is_active', 'company', 'kudos_left')

    def get_kudos_left(self, instance):
        today = datetime.now()
        kudos_last_week = Kudos.objects.filter(from_user=instance.id, created__week=today.isocalendar()[1])
        kudos_left = 3 - len(kudos_last_week)
        return kudos_left

class KudosSerializer(serializers.ModelSerializer):
    from_user_id = serializers.IntegerField(write_only=True)
    to_user_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Kudos
        depth=1
        fields = ('id', 'message','from_user','to_user', 'from_user_id', 'to_user_id')
