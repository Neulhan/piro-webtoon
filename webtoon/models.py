from django.db import models
# Create your models here.


class Webtoon(models.Model):
    title = models.CharField(max_length=255)
    list_url = models.URLField()
    thumb_src = models.URLField()

    def __str__(self):
        return self.title


class Episode(models.Model):
    webtoon = models.ForeignKey(Webtoon, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    thumb_src = models.URLField()
    ep_url = models.URLField()

    def __str__(self):
        return self.title


class Cut(models.Model):
    ep = models.ForeignKey(Episode, on_delete=models.CASCADE)
    cut_src = models.URLField()
    num = models.IntegerField()

