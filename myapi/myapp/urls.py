from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^musics/$', views.MusicList.as_view(), name='music-list'),
    url(r'^music/(?P<pk>[0-9]+)/$', views.MusicDetail.as_view(), name='music-detail'),

    url(r'^albuns/$', views.AlbumList.as_view()),
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumDetail.as_view()),

    url(r'^bands/$', views.BandList.as_view()),
    url(r'^band/(?P<pk>[0-9]+)/$', views.BandDetail.as_view()),

    url(r'^members/$', views.MemberList.as_view()),
    url(r'^member/(?P<pk>[0-9]+)/$', views.MemberDetail.as_view()),
]