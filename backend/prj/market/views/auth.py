from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

from drf_yasg.utils import swagger_auto_schema


class CommonResponceSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    message = serializers.CharField()


class LoginRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class AuthViews(APIView):
    '''
        User login
    '''
    @swagger_auto_schema(
        request_body = LoginRequestSerializer,
        responses = {200: CommonResponceSerializer}
    )
    def post(self, request):
        return Response(LoginRequestSerializer({
            'status': 0,
            'message': 'Gooood'
        }))


from rest_framework.decorators import api_view


def hello(request):
    return Response({"message": "hello"})