# views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import Order
def get_order_status(request, order_id):
    order = Order.objects.get(pk=order_id)
    return JsonResponse({'status': order.status})
def place_order(request):
    # Simulate order placement (create a new order)
    order = Order.objects.create(
        customer_name='John Doe',
        product_name='Example Product',
        status='placed'
    )
    order_id = order.id
    return JsonResponse({'order_id': order_id, 'status': 'Order Placed'})

def update_to_in_progress(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.status = 'in_progress'
    order.save()
    return JsonResponse({'status': 'In Progress'})

def update_to_delivered(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.status = 'delivered'
    order.save()
    return JsonResponse({'status': 'Delivered'})
