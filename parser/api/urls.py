from api import viewsets
from parser.urls import router

router.register('file', viewsets.FileViewSet)
router.register('filestotal', viewsets.FilesTotalViewSet, basename='Totals')
router.register('filesdata', viewsets.FilesDataViewSet, basename='Detail_date')

urlpatterns = []
