from rest_framework import serializers
from .models import Robot


class RobotSerializer(serializers.ModelSerializer):
    serial = serializers.ReadOnlyField()

    class Meta:
        model = Robot
        fields = "__all__"

    def create(self, validated_data):
        serial = f"{validated_data['model']}-{validated_data['version']}"
        validated_data["serial"] = serial
        robot = Robot.objects.create(**validated_data)
        return robot
