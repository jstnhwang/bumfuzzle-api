from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from .models import Question
from .serializers import QuestionSerializer

@api_view(['GET', 'POST', 'DELETE'])
def questions(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"id": serializer.data["id"]}, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        Question.objects.all().delete()
        return JsonResponse({"result": "success"})

@api_view(['GET', 'DELETE'])
def question(request, pk):
    if request.method == 'GET':
        question = Question.objects.get(pk=pk)
        serializer = QuestionSerializer(question)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'DELETE':
        question = Question.objects.get(pk=pk)
        Question.objects.filter(question__description=question.description).delete()
        return JsonResponse({"result": "success"})