from rest_framework.serializers import ModelSerializer

from .models import Worker, Item

class WorkerSerializer(ModelSerializer):
    class Meta:
        model = Worker
        fields = ('id', "name", "designation", "work_number")


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ("id", "name","cost")