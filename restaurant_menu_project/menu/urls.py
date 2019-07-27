from django.urls import path
from . import views

urlpatterns = [
    path('api/menu/', views.MenuListCreate.as_view()),

]
