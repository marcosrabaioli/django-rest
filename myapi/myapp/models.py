from django.db import models

# Create your models here.


class Music(models.Model):

    class Meta:

        db_table = 'music'

    title = models.CharField(max_length=200)
    seconds = models.IntegerField()
    album = models.ForeignKey('Album', related_name='musics')

    def __str__(self):
        return self.title


class Album(models.Model):

    class Meta:
        db_table = 'album'

    title = models.CharField(max_length=200)
    band = models.ForeignKey('Band', related_name='albuns')
    date = models.DateField()


class Band(models.Model):

    class Meta:
        db_table = 'band'

    name = models.CharField(max_length=200)


class Member(models.Model):

    class Meta:
        db_table = 'member'

    name = models.CharField(max_length=200)
    age = models.IntegerField()
    band = models.ForeignKey('Band', related_name='members')