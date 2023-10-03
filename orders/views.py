from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order
from .serializers import OrderSerializer
import json


# Создание нового заказа
@csrf_exempt
def create_order(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            serializer = OrderSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(
                    {"message": "The order was successfully created"}, status=201
                )
            else:
                return JsonResponse({"error": serializer.errors}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Incorrect JSON format"}, status=400)
    else:
        return JsonResponse({"error": "The method is not supported"}, status=405)


# Получение списка всех заказов
def list_orders(request):
    if request.method == "GET":
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({"error": "The method is not supported"}, status=405)


# Получение информации о конкретном заказе
def get_order(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
        serializer = OrderSerializer(order)
        return JsonResponse(serializer.data)
    except Order.DoesNotExist:
        return JsonResponse({"error": "Order not found"}, status=404)


# Обновление информации о заказе
@csrf_exempt
def update_order(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        return JsonResponse({"error": "Order not found"}, status=404)

    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            serializer = OrderSerializer(order, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(
                    {"message": "The order has been successfully updated"}, status=200
                )
            else:
                return JsonResponse({"error": "Incorrect data"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Incorrect JSON format"}, status=400)
    elif request.method == "PATCH":
        try:
            data = json.loads(request.body)
            serializer = OrderSerializer(order, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(
                    {"message": "The order has been successfully updated"}, status=200
                )
            else:
                return JsonResponse({"error": "Incorrect data"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Incorrect JSON format"}, status=400)
    else:
        return JsonResponse({"error": "The method is not supported"}, status=405)


# Удаление заказа
@csrf_exempt
def delete_order(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
        order.delete()
        return JsonResponse(
            {"message": "The order was successfully removed"}, status=204
        )
    except Order.DoesNotExist:
        return JsonResponse({"error": "Order not found"}, status=404)
