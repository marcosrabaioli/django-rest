from rest_framework import generics
from .models import Music
from .serializers import MusicSerializer

# Create your views here.
class MusicList(generics.ListCreateAPIView):

    queryset = Music.objects.all()
    serializer_class = MusicSerializer
