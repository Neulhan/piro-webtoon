from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from webtoon.models import *


@admin.register(Webtoon)
class WebtoonAdmin(ImportExportModelAdmin):
    pass


@admin.register(Episode)
class EpisodeAdmin(ImportExportModelAdmin):
    pass


@admin.register(Cut)
class CutAdmin(ImportExportModelAdmin):
    pass
