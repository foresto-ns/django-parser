import os
import uuid

from django.db import models


def create_file_name(instance, filename):
    """Функция по генерации названия файла и охранение в нужной папке"""
    fname, ext = os.path.splitext(filename)
    file_id = str(instance.id) + ext
    path = f'{file_id[:2]}/{file_id[2:4]}/{file_id}'
    return path


class FileModel(models.Model):
    """Модель загрузки файлов в папку static/media"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    filepath = models.FileField(blank=False, null=False, upload_to=create_file_name, verbose_name='Путь к файлу')
    name = models.CharField(max_length=256, editable=True, null=True, blank=True, default='',
                            verbose_name='Название файла в системе')
    upload_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"


class FilesDataModel(models.Model):
    """Модель пришедших данных в файле"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.ForeignKey(FileModel, on_delete=models.SET_NULL, null=True, verbose_name='Загруженный файл')
    record_id = models.IntegerField(verbose_name='id записи в файле')
    company = models.CharField(max_length=256, verbose_name='Название компании')
    date = models.DateTimeField(verbose_name='Первая дата')
    fact_qliq_data1 = models.DecimalField(max_digits=256, decimal_places=0,
                                          verbose_name='Фактические данные по Qliq за первую дату')
    fact_qliq_data2 = models.DecimalField(max_digits=256, decimal_places=0,
                                          verbose_name='Фактические данные по Qliq за вторую дату')
    fact_qoil_data1 = models.DecimalField(max_digits=256, decimal_places=0,
                                          verbose_name='Фактические данные по Qoil за первую дату')
    fact_qoil_data2 = models.DecimalField(max_digits=256, decimal_places=0,
                                          verbose_name='Фактические данные по Qoil за вторую дату')
    forecast_qliq_data1 = models.DecimalField(max_digits=256, decimal_places=0,
                                              verbose_name='Прогнозируемые данные по Qliq за первую дату')
    forecast_qliq_data2 = models.DecimalField(max_digits=256, decimal_places=0,
                                              verbose_name='Прогнозируемые данные по Qliq за вторую дату')
    forecast_qoil_data1 = models.DecimalField(max_digits=256, decimal_places=0,
                                              verbose_name='Прогнозируемые данные по Qoil за первую дату')
    forecast_qoil_data2 = models.DecimalField(max_digits=256, decimal_places=0,
                                              verbose_name='Прогнозируемые данные по Qoil за вторую дату')

    class Meta:
        verbose_name = "Данные"
        verbose_name_plural = "Данные"

