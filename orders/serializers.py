from rest_framework import serializers
from robots.models import Robot
from .models import Order
from customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.DictField(
        child=serializers.CharField(max_length=255)
    )  # Используем DictField для передачи данных клиента

    class Meta:
        model = Order
        fields = ["customer", "robot_serial"]

    # def validate_robot_serial(self, value):
    #     # Попытка получить робота с указанным серийным номером
    #     robot = Robot.objects.filter(serial=value).first()
    #
    #     if not robot:
    #         raise serializers.ValidationError(
    #             "Робот с указанным серийным номером не существует."
    #         )
    #
    #     return value

    def create(self, validated_data):
        # Извлекаем данные клиента из validated_data
        customer_data = validated_data.pop("customer", {})

        # Извлекаем email из данных клиента
        email = customer_data.get("email")

        # Проверяем, существует ли клиент с указанным email
        try:
            customer = Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            # Если клиента с указанным email нет, создаем его
            customer = Customer.objects.create(email=email)

        # Извлекаем серийный номер робота
        robot_serial = validated_data.get("robot_serial")

        # Попытка получить робота с указанным серийным номером
        robot = Robot.objects.filter(serial=robot_serial).first()

        if robot:
            # Если робот существует, удаляем его
            robot.delete()
        else:
            # Если робота с указанным серийным номером нет, создаем заказ
            order = Order.objects.create(customer=customer, **validated_data)
            return order

        return robot  # Если робот был удален, не создаем заказ
