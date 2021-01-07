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

    def get_queryset(self, sorting_col=None):
        if sorting_col:
            sorting_col = sorting_col.replace('-', '_')

            if sorting_col == 'moved_by':
                return Application.objects.order_by(
                    sorting_col + '__first_name',
                    sorting_col + '__last_name'
                )

            if sorting_col in ('technology', 'status'):
                sorting_col += '__name'
            return Application.objects.order_by(sorting_col)

        else:
            return Application.objects.all().order_by('-applied_on')

    def get(self, request, format=None):
        queryset = self.get_queryset(request.GET.get('sort'))
        serializer = ApplicationSerializer(queryset, many=True)
        return Response(serializer.data)
