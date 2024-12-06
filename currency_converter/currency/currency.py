from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .external_api import convert_currency, get_exchange_rates
from .models.schemas import CurrencyConvert

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def exchange_rates(request):
    try:
        rates = get_exchange_rates()  # Получаем курсы валют
        return Response(rates)  # Возвращаем курсы валют в ответе
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def convert(request):
    # Используем модель Pydantic для валидации входящих данных
    data = CurrencyConvert(**request.data)
    
    try:
        converted_amount = convert_currency(data.amount, data.from_currency, data.to_currency)
        return Response({'converted_amount': converted_amount})
    except ValueError as e:
        return Response({'error': str(e)}, status=400)
    except Exception as e:
        return Response({'error': str(e)}, status=500)