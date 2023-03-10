import decimal
import datetime
import os

import pandas as pd
from django.db.models import F, Sum

from api.models import FilesDataModel, FileModel
from parser import settings


def calc_total() -> list[dict[str, datetime.datetime | decimal.Decimal]]:
    """
    Расчет прогнозируемых тоталов по Qoil и Qliq
    :return: список сумм Qoil и Qliq по датам
    """
    data = FilesDataModel.objects \
        .values('date') \
        .annotate(qliq_total=F('forecast_qliq_data1') + F('forecast_qliq_data2'),
                  qoil_total=F('forecast_qoil_data1') + F('forecast_qoil_data2')) \
        .annotate(qliq_total=Sum('qliq_total'), qoil_total=Sum('qoil_total')) \
        .order_by('date') \
        .distinct()
    return data


def parse_file(file_id: str) -> None:
    """
    Парсинг данных из файла и сохранение их
    :param file_id: id присланного файла
    :return: None
    """
    if not file_id:
        return None
    try:
        file = FileModel.objects.get(id=file_id)
    except FileModel.DoesNotExist:
        return None
    filname = os.path.join(settings.MEDIA_ROOT, str(file.filepath))

    dataframe = pd.read_excel(filname, skiprows=2)

    for row in dataframe.iterrows():
        FilesDataModel.objects.create(
            file=file,
            record_id=row[1][0],
            company=row[1][1],
            date=datetime.datetime(2023, 1, row[0]%30+1),
            fact_qliq_data1=row[1][2],
            fact_qliq_data2=row[1][3],
            fact_qoil_data1=row[1][4],
            fact_qoil_data2=row[1][5],
            forecast_qliq_data1=row[1][6],
            forecast_qliq_data2=row[1][7],
            forecast_qoil_data1=row[1][8],
            forecast_qoil_data2=row[1][9],
        )
