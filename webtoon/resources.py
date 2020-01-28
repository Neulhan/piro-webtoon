from import_export import resources
from .models import *


class WebtoonResource(resources.ModelResource):
    class Meta:
        model = Webtoon


class EpisodeResource(resources.ModelResource):
    class Meta:
        model = Episode


class CutResource(resources.ModelResource):
    class Meta:
        model = Cut
