import re
from django.http import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from . import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, Format=None):
        """return list of some values"""

        an_api = ['Hello', 'How are you', 'This is working']

        return Response({'message': 'lets see', 'api_data': an_api})

    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Hello '+name
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating the object"""
        return Response({'message': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial updating the object"""
        return Response({'message': 'PATCH'})

    def delete(self, request, pk=None):
        """Handle deleting the object"""
        return Response({'message': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """test API Viewsets"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
            'uses actions {list,create,retrieve,update, partial_update}',
            'automatically maps to URLs using routers',
            'provides more fucntionality with less code'
        ]

        return Response({'message': 'hello', 'a_viewset': a_viewset})

    def create(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Hello '+name
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})
