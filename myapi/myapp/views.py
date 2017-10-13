from .models import Music, Album, Band, Member
from .serializers import MusicSerializer, AlbumSerializer, MemberSerializer, BandSerializer
from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_condition import Or
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication
from rest_framework.authentication import SessionAuthentication


class AlbumFilter(filters.FilterSet):

    date_gte = filters.DateFilter(name="date", lookup_expr='gte')
    date_lte = filters.DateFilter(name="date", lookup_expr='lte')

    class Meta:

        model = Album
        fields = '__all__'

class MusicList(generics.ListCreateAPIView):

    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class MusicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

class AlbumList(generics.ListCreateAPIView):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = AlbumFilter


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'



class BandList(generics.ListCreateAPIView):

    queryset = Band.objects.all()
    serializer_class = BandSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class BandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all_'


class MemberList(generics.ListCreateAPIView):

    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = MemberSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all_'