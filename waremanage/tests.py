from django.test import TestCase, Client, client
from django.urls import reverse
from rest_framework import status
from .serializers import ItemSerializer, WorkerSerializer
from .models import Worker, Item
import json
# Create your tests here.

client = Client()

class TestWorkerandItem(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        Worker.objects.create(name="king", designation="manager", work_number="M234")

        Item.objects.create(name="milo", cost=200)

    def test_worker_name(self):
        obj = Worker.objects.get(id=1)
        self.assertEquals("king", f"{obj.name}")

    def test_worker_designation(self):
        obj = Worker.objects.get(id=1)
        self.assertEquals("manager", f"{obj.designation}")

    def test_worker_work_number(self):
        obj = Worker.objects.get(id=1)
        self.assertEquals("M234", f"{obj.work_number}")

    def test_item_name(self):
        obj = Item.objects.get(id=1)
        self.assertEquals("milo", f"{obj.name}")

    def test_item_cost(self):
        obj = Item.objects.get(id=1)
        self.assertEquals(200, obj.cost)


class TestRoutes(TestCase):

    def setUp(self) -> None:
        self.king = Worker.objects.create(name="king", designation="manager", work_number="M234")
        self.queen = Worker.objects.create(name="queen", designation="manager", work_number="M235")
        self.prince = Worker.objects.create(name="prince", designation="loader", work_number="L234")

        self.milo = Item.objects.create(name="milo", cost=200)
        Item.objects.create(name="orange", cost=300)
        Item.objects.create(name="milk", cost=500)

    def test_all_items_listed(self):
        response = client.get(reverse('list_all_items'))
        obj = Item.objects.all()
        ser = ItemSerializer(obj, many=True)
        self.assertEquals(response.data, ser.data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_item_listed(self):
        response = client.get(reverse('get_item', kwargs={'pk':self.milo.name}))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_all_workers_listed(self):
        response = client.get(reverse('list_all_workers'))
        obj = Worker.objects.all()
        ser = WorkerSerializer(obj, many=True)
        self.assertEquals(response.data, ser.data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_worker_listed(self):
        response = client.get(reverse('get_worker', kwargs={'pk':self.king.name}))
        self.assertEquals(response.status_code, status.HTTP_200_OK)