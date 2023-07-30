from django.urls import path
from . import views

urlpatterns = [
    path('', views.FileListCreate.as_view()),
    path('<int:pk>/', views.FileRetrieveUpdateDestroy.as_view()),
    path('file/<int:pk>/delete/', views.FileDestroy.as_view()),  # Agregar esta línea
]
