from allauth.account.views import LoginView
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import ApplicationDetail


class CustomLoginView(LoginView):
    """
    Changes the default login template from Django-Allauth
    """
    template_name = 'dashboard/login.html'


@method_decorator(login_required, name='dispatch')
class DashboardView(generic.TemplateView):
    """
    Dashboard View uses ajax to load data from API views,
    hence a template view is used here.
    """
    template_name = 'dashboard/index.html'


@method_decorator(login_required, name='dispatch')
class SingleApplicationView(generic.DetailView):
    model = ApplicationDetail
    template_name = 'dashboard/single_application.html'
    context_object_name = 'application'
