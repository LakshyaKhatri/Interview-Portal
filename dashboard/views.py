from allauth.account.views import LoginView
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class CustomLoginView(LoginView):
    """
    Changes the default login template from Django-Allauth
    """
    template_name = 'interview_portal/login.html'


@method_decorator(login_required, name='dispatch')
class DashboardView(generic.TemplateView):
    template_name = 'interview_portal/index.html'
