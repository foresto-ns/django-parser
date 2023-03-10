from django.db.models import Sum, F

from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from api import serializers
from api.models import FileModel, FilesDataModel
from api.utils import calc_total, parse_file


class FileViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = FileModel.objects.all()
    serializer_class = serializers.FileSerializer

    def create(self, request, *args, **kwargs) -> Response:
        """Переопределение метода POST для добавления функций и методов для парсинга и расчета тоталов"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        parse_file(file_id=serializer.data.get('id'))
        data = calc_total()
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class FilesDataViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Просмотр информации по файлам"""
    queryset = FilesDataModel.objects.all()
    serializer_class = serializers.FilesDataSerializer
    filterset_fields = ['file', 'file__name']


class FilesTotalViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Просмотр тоталов"""
    queryset = FilesDataModel.objects \
        .values('date') \
        .annotate(qliq_total=F('forecast_qliq_data1') + F('forecast_qliq_data2'),
                  qoil_total=F('forecast_qoil_data1') + F('forecast_qoil_data2')) \
        .annotate(qliq_total=Sum('qliq_total'), qoil_total=Sum('qoil_total')) \
        .order_by('date') \
        .distinct()
    serializer_class = serializers.FilesTotaSerializer
    filterset_fields = ['file', 'file__name']
