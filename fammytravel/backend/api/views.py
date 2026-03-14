from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def health_check(request):
    return Response({
        'status': 'ok',
        'message': 'Fammytravel API is running'
    })


@api_view(['GET'])
def destinations(request):
    return Response({
        'destinations': [
            {'id': 1, 'name': 'Switzerland', 'slug': 'switzerland'},
            {'id': 2, 'name': 'Japan', 'slug': 'japan'},
        ]
    })
