from rest_framework.decorators import api_view
from rest_framework.response import Response


def index(request):
    return Response({"message": "Hello, world!"})
