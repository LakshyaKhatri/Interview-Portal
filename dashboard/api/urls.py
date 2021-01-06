from django.urls import path
from .views import ApplicationListAPIView

urlpatterns = [
    path('applications/', ApplicationListAPIView.as_view())
]
