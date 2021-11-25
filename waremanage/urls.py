from django.urls import path
from .views import create_new_item, create_new_worker, list_all_items, list_all_workers, get_item, get_worker


urlpatterns = [
    path('items/', list_all_items),
    path('items/<str:pk>/', get_item),
    path('items/new/', create_new_item),
    path('workers/', list_all_workers),
    path('workers/<str:pk>/', get_worker),
    path('workers/new/', create_new_worker)
]