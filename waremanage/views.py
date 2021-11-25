from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import Worker, Item
from .serializers import ItemSerializer, WorkerSerializer, WorkerSerializer
# Create your views here.


def _create_object(request, serializer):
    """a factory method that allows for creaton of new database objects
       it is a generic method and can be extended to do more (please don't break)    
    """
    obj = serializer(request.data)
    if obj.is_valid():
        return Response({"message": "created successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def _list_data_objects(request, model, serializer):
    """a factory method for querying and receiving database objects"""
    obj = model.objects.all()
    ser = serializer(obj, many=True)
    return Response(ser.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def list_all_items(request):
    return _list_data_objects(request, Item, ItemSerializer)

@api_view(["GET", "PUT", "DELETE"])
def get_item(request, pk: str):
    try:
        obj = Item.objects.get(name=pk)
    except Item.DoesNotExist:
        return Response({f"message:  {pk} does not exist"},status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ItemSerializer(obj)
        if serializer.is_valid():
            return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = ItemSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)

    elif request.method == "DELETE":
        obj.delete()
        return Response({"message": "deleted successfully"},status=status.HTTP_200_OK)
    
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def create_new_item(request):
    return _create_object(request, ItemSerializer)


@api_view(["GET"])
def list_all_workers(request):
    return _list_data_objects(request, Worker, WorkerSerializer)


@api_view(["GET", "POST" "PUT", "DELETE"])
def get_worker(request, pk: str):
    try:
        obj = Worker.objects.get(name=pk)
    except Worker.DoesNotExist:
        return Response({f"message:  {pk} does not exist"},status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = WorkerSerializer(obj)
        if serializer.is_valid():
            return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        return _create_object(request, WorkerSerializer)

    elif request.method == "PUT":
        serializer = WorkerSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)

    elif request.method == "DELETE":
        obj.delete()
        return Response({"message": "deleted successfully"},status=status.HTTP_200_OK)
    
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def create_new_worker(request):
    return _create_object(request, WorkerSerializer)