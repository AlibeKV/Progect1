from telnetlib import STATUS
from rest_framework.decorators import api_view 
from rest_framework import status
from rest_framework.response import Response
#from .permissions import EventPermission, EventDetailPermission
from app.models import Event
from .serializers import EventSerializer
from api import serializers

@api_view(['GET , POST'])
#@permission_classes([EventPermission])
def event(request):

    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=200)
    elif request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, STATUS=201)
        return Response(serializer.errors, status=201)
@api_view(['GET , PUT' ,'DELETE'])
#@permission_classes([EventDetailPermission])
def event_detail(request,pk):

    event = Event.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = EventSerializer(event)
        return Response(serializer.data, status=202)
    elif request.method == 'PUT':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=202)
    elif request.method == 'DELETE':
        event.delete()
        return Response(status=204)


