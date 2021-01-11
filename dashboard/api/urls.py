from django.urls import path
from .views import ApplicationListAPIView, update_status_apiview

urlpatterns = [
    path('applications/', ApplicationListAPIView.as_view()),
    path('update-status/<int:pk>/', update_status_apiview),
]
