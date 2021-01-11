from django.urls import path
from .views import (
    CustomLoginView,
    DashboardView,
    SingleApplicationView,
)

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', DashboardView.as_view(), name='dashboard'),
    path('<int:pk>/', SingleApplicationView.as_view())
]
