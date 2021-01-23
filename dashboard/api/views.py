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
