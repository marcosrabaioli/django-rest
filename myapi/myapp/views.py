from .models import Music, Album, Band, Member
from .serializers import MusicSerializer, AlbumSerializer, MemberSerializer, BandSerializer
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny


class MusicList(generics.ListCreateAPIView):

    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )


class MusicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )


class AlbumList(generics.ListCreateAPIView):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )


class BandList(generics.ListCreateAPIView):

    queryset = Band.objects.all()
    serializer_class = BandSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )


class BandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )


class MemberList(generics.ListCreateAPIView):

    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = MemberSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )
