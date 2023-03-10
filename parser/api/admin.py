from django.contrib import admin

from api import models

admin.site.register(models.FileModel)
admin.site.register(models.FilesDataModel)
