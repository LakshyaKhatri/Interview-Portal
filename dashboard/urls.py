from django.urls import path
from django.views.generic import TemplateView
from .views import CustomLoginView

app_name = 'dashboard'
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', TemplateView.as_view(template_name='interview_portal/index.html'), name='home'),
]
