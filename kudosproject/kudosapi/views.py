from rest_framework import viewsets
from .serializer import UserSerializer, KudosSerializer
from .models import User, Kudos

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class KudosViewSet(viewsets.ModelViewSet):
    queryset = Kudos.objects.all()
    serializer_class = KudosSerializer
