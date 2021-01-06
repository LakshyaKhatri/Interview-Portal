from allauth.account.views import LoginView
from django.views import generic
from .models import Application
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class CustomLoginView(LoginView):
    """
    Changes the default login template from Django-Allauth
    """
    template_name = 'interview_portal/login.html'


@method_decorator(login_required, name='dispatch')
class ApplicationListView(generic.ListView):
    model = Application
    template_name = 'interview_portal/index.html'
    context_object_name = 'applications'
