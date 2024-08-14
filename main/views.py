
"""
Views for creating endpoins.
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


class HelloWorld(APIView):
    """
    A simple test endpoint.
    """

    def get(self, request, format=None):
        """GET METHOD."""
        return Response("Hello world!")