from django.urls import path

from orders.views import create_order, update_order, delete_order, get_order

urlpatterns = [
    path("create_order/", create_order, name="create_order"),
    path("get_order/", get_order, name="create_order"),
    path("update_order/<int:pk>/", update_order, name="update_order"),
    path("delete_order/<int:pk>/", delete_order, name="delete_order"),
]
