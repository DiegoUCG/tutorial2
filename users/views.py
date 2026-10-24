from rest_framework.decorators import api_view
from rest_framework.response import response 
from .serializers import userserializers

user = {
    "name": "Dieguito",
    "password": "1234"
}

@api_view(["GET"])
def get_users(request):
    return response(userserializers(user) .data)
