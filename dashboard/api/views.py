from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ApplicationSerializer
from dashboard.models import Application, Status
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from rest_framework import status as http_status


@method_decorator(login_required, name='dispatch')
class ApplicationListAPIView(APIView):
    """
    Takes request, modifies the application list query according
    to the sort keyword provided and returns a JSON response.
    """
    serializer_class = ApplicationSerializer

    def get_db_col_name(self, sort_kw):
        """
        Takes a sort keyword and returns corrosponding
        column name suitable for db queries.
        """
        if not sort_kw:
            return ('-applied_on', )
        sort_kw = sort_kw.replace('-', '_')
        sort_kw = '-' + sort_kw[1:] if sort_kw.startswith('_') else sort_kw

        if sort_kw in ('technology', 'status'):
            sort_kw += '__name'
            return (sort_kw,)
        if sort_kw == 'moved_by':
            return (
                sort_kw + '__first_name',
                sort_kw + '__last_name'
            )

        return (sort_kw, )

    def get_queryset(self, sorting_cols):
        return Application.objects.order_by(*sorting_cols)

    def get(self, request, format=None):
        db_col_name = self.get_db_col_name(request.GET.get('sort'))
        queryset = self.get_queryset(db_col_name)
        serializer = ApplicationSerializer(queryset, many=True)
        return Response(serializer.data)


@login_required
@api_view(['GET', 'POST'])
def update_status_apiview(request, pk):
    current_application = None
    application_status = None

    try:
        current_application = Application.objects.get(pk=pk)
        application_status = Status.objects.get(pk=request.data.get('status'))
        current_application.status = application_status
        current_application.save()
        return Response({'message': 'Status updated successfully'})

    except Application.DoesNotExist:
        return Response({'message': 'Application not found'}, status=http_status.HTTP_404_NOT_FOUND)

    except Status.DoesNotExist:
        return Response({'message': 'Status not found'}, status=http_status.HTTP_404_NOT_FOUND)
