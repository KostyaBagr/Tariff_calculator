
"""
Views for creating endpoins.
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import TariffInputSerializer
from .services import tariffService


class CalculatorView(APIView):
    """
    Endpoint for calculation.
    """
    def post(self, request, format=None) -> Response:
        serializer = TariffInputSerializer(data=request.data)
        if serializer.is_valid():
            return Response(tariffService(serializer), status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)