from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, Format=None):
        """return list of some values"""

        an_api = ['Hello', 'How are you', 'This is working']

        return Response({'message': 'lets see', 'api_data': an_api})
