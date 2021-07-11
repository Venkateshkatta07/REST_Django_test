from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
