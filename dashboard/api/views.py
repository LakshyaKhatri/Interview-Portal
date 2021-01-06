from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ApplicationSerializer
from dashboard.models import Application
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class ApplicationListAPIView(APIView):
    """
    Takes request, modifies the application list query according
    to the sort keyword provided and returns a JSON response.
    """
    serializer_class = ApplicationSerializer

    def get_queryset(self, sorting_col='-applied_on'):
        return Application.objects.all().order_by(sorting_col)

    def get(self, request, format=None):
        queryset = self.get_queryset()
        serializer = ApplicationSerializer(queryset, many=True)
        return Response(serializer.data)
