from allauth.account.views import LoginView


class CustomLoginView(LoginView):
    """
    Changes the default login template from Django-Allauth
    """
    template_name = 'interview_portal/login.html'
