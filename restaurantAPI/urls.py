from django.urls import path, include
from . import views 
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]