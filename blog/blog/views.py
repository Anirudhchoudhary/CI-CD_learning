from django.shortcuts import render
from django.http import JsonResponse


def home(request):
    print(request)
    return JsonResponse(data={"message": "Anirudh",
                              "status": 200})
