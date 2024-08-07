from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from .serializers import PeopleSerializers


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        responseObj = Person.objects.all()
        personSerializer = PeopleSerializers(responseObj, many= True)
        return Response(personSerializer.data)
    else :
        print(request.data)
        data = request.data
        personSerializer = PeopleSerializers(data = data)
        print(personSerializer)
        if personSerializer.is_valid():
            personSerializer.save()
            return Response(personSerializer.data)
        else:
            return Response(personSerializer.errors)
