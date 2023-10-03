from django.urls import path
from .views import (
    create_robot,
    list_robots,
    update_robot,
    delete_robot,
    generate_summary_excel,
)

urlpatterns = [
    path("create-robot/", create_robot, name="create-robot"),
    path("list-robots/", list_robots, name="list-robots"),
    path("update-robot/<int:robot_id>/", update_robot, name="update-robot"),
    path("delete-robot/<int:robot_id>/", delete_robot, name="delete-robot"),
    path("summary-excel/", generate_summary_excel, name="generate-summary-excel"),
]
