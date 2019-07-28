from .models import Menu
from .serializers import MenuSerializer, MenuQueryParams
from rest_framework.views import APIView
from rest_framework.response import Response


class MenuListCreate(APIView):

    def get(self, request):
        query_params = MenuQueryParams(data=request.query_params)
        if not query_params.is_valid():
            return Response({'error': 'wrong query params'}, status=400)
        queryset = Menu.objects.all().order_by('id')
        search = query_params.data.get('search')
        ordering = query_params.data.get('ordering')
        if search:
            queryset = queryset.filter(dish__icontains=search)

        if ordering:
            queryset = queryset.order_by(ordering)

        serializer = MenuSerializer(queryset, many=True)

        return Response(serializer.data)
