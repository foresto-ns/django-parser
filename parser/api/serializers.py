from rest_framework import serializers

from api.models import FileModel, FilesDataModel


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = '__all__'


class FilesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilesDataModel
        fields = '__all__'


class FilesTotaSerializer(serializers.Serializer):
    date = serializers.DateTimeField(read_only=True)
    qliq_total = serializers.DecimalField(max_digits=256, decimal_places=0, read_only=True)
    qoil_total = serializers.DecimalField(max_digits=256, decimal_places=0, read_only=True)
