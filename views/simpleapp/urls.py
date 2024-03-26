from django.urls import path
from .views import ProductsList, ProductDetail


urlpatterns = [
   path('', ProductsList.as_view()),
   path('<int:id>', ProductDetail.as_view()),
]