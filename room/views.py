from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from .models import Room
from .serializers import RoomSerializer

@api_view(['GET', 'POST'])
def rooms(request):
    print(request)
    if request.method == 'GET':
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        if(data["is_public"] == False and not data["password"]):
          return JsonResponse({'error': 'Password should be typed on private rooms'}, status=400)
        
        serializer = RoomSerializer(data=data)
        if serializer.is_valid():  
            serializer.save()
            return JsonResponse({"id": serializer.data["id"]}, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Room.objects.all().delete()
        return JsonResponse({"result": "success"})

@api_view(["GET"])
def room(request, pk):
    if request.method == 'GET':
        room = Room.objects.get(pk=pk)
        serializer = RoomSerializer(room)
        return JsonResponse(serializer.data, safe=False)