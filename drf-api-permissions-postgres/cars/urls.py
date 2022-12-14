from django.urls import path

from .views import CarListView, CarDetailView,SellerListView,SellerDetailView

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('seller/', SellerListView.as_view(), name='seller_list'),
    path('seller/<int:pk>/', SellerDetailView.as_view(), name='seller_detail'),
]