from django.urls import path, include 
from rest_framework import routers 

from users.views import (
    get_users
)

router = routers.DefaultRouter()
router.register()

urlpatterns = [
    path("",include(router.urls)),
    path("users/example/", get_users, name="get_users_example")
]